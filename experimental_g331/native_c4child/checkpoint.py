from __future__ import annotations
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import json,hashlib
from .graph import C4Graph
from .dynamic_h3 import DynamicBoundTrace,BinaryTraceTemplate

SCHEMA='C4M_CHILD_V0.3'
SCHEMA_COMPACT='C4M_CHILD_V0.4_COMPACT'
SUPPORTED={'C4M_CHILD_V0.1','C4M_CHILD_V0.2','C4M_CHILD_V0.3',SCHEMA_COMPACT}

def _jbytes(obj):return json.dumps(obj,ensure_ascii=False,separators=(',',':'),sort_keys=True).encode('utf-8')

def save_c4m(path,graph:C4Graph,h3:DynamicBoundTrace|None=None,meta=None,runtime_state=None,organs=None):
    path=Path(path);h3=h3 or DynamicBoundTrace();meta=meta or {}
    graph_bytes=_jbytes(graph.to_dict())
    h3_bytes=_jbytes({'schema':'H3_DYNAMIC_TEMPLATE_V0.1','template':{'alpha':h3.t.alpha,'w0':h3.t.w0,'w1':h3.t.w1},'transient_persisted':False})
    files={'graph.json':graph_bytes,'h3_templates.json':h3_bytes}
    if runtime_state is not None:files['runtime_state.json']=_jbytes(runtime_state)
    for name,obj in (organs or {}).items():
        safe=str(name).strip().replace('..','_').strip('/')
        if not safe: raise ValueError('bad organ name')
        files[f'organs/{safe}.json']=_jbytes(obj)
    manifest={'schema':SCHEMA,'meta':meta,'files':sorted(files),'sha256':{k:hashlib.sha256(v).hexdigest() for k,v in files.items()}}
    with ZipFile(path,'w',ZIP_DEFLATED) as z:
        z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True))
        for k,v in files.items():z.writestr(k,v)
    return manifest

def load_c4m(path,with_runtime=False,with_organs=False):
    with ZipFile(path,'r') as z:
        manifest=json.loads(z.read('manifest.json'))
        schema=manifest.get('schema')
        if schema not in SUPPORTED:raise ValueError('unsupported c4m schema')
        if schema=='C4M_CHILD_V0.1':
            gb=z.read('graph.json');hb=z.read('h3_templates.json')
            if hashlib.sha256(gb).hexdigest()!=manifest['graph_sha256']:raise ValueError('graph checksum mismatch')
            if hashlib.sha256(hb).hexdigest()!=manifest['h3_sha256']:raise ValueError('h3 checksum mismatch')
            runtime_state=None
        else:
            raw={name:z.read(name) for name in manifest['files']}
            for name,b in raw.items():
                if hashlib.sha256(b).hexdigest()!=manifest['sha256'][name]:raise ValueError(f'{name} checksum mismatch')
            gb=raw['graph.json'];hb=raw['h3_templates.json']
            runtime_state=json.loads(raw['runtime_state.json']) if 'runtime_state.json' in raw else None
    g=C4Graph.from_dict(json.loads(gb));hd=json.loads(hb)['template'];h=DynamicBoundTrace(BinaryTraceTemplate(**hd))
    organs={}
    if schema!='C4M_CHILD_V0.1':
        for name,b in raw.items():
            if name.startswith('organs/') and name.endswith('.json'):
                organs[name[len('organs/'):-len('.json')]]=json.loads(b)
    if with_runtime and with_organs:return g,h,manifest,runtime_state,organs
    if with_runtime:return g,h,manifest,runtime_state
    if with_organs:return g,h,manifest,organs
    return g,h,manifest


def _hot_cold_graph_dicts(graph:C4Graph):
    full=graph.to_dict()
    active_ids={row[-1] for row in full.get('canonical',[])}
    # Strict constitution keeps source assertions hot as part of the continuous
    # epistemic life-line. They are not canonical truth (no canonical slot),
    # but must remain queryable after restart rather than disappearing into cold history.
    active_ids.update(x.get('fact_id') for x in full.get('facts',[]) if x.get('status') in {'SOURCE_ASSERTED','SOURCE_SUPERSEDED'})
    hot=dict(full)
    hot['facts']=[x for x in full.get('facts',[]) if x.get('fact_id') in active_ids]
    hot['audit']=[]
    cold={'schema':'C4_GRAPH_COLD_HISTORY_V0.1',
          'facts':[x for x in full.get('facts',[]) if x.get('fact_id') not in active_ids],
          'audit':full.get('audit',[])}
    return hot,cold

def save_c4m_compact(path,graph:C4Graph,h3:DynamicBoundTrace|None=None,meta=None,runtime_state=None,organs=None,include_cold=True):
    """V0.4 checkpoint: fast hot startup with optional cold history in the same zip."""
    path=Path(path);h3=h3 or DynamicBoundTrace();meta=meta or {}
    hot,cold=_hot_cold_graph_dicts(graph)
    src=getattr(graph,'_unhydrated_cold_source',None)
    if src:
        with ZipFile(src,'r') as z0:
            old_cold=json.loads(z0.read('cold/history.json'))
        seen={x.get('fact_id') for x in cold['facts']}|{x.get('fact_id') for x in hot['facts']}
        cold['facts']=[x for x in old_cold.get('facts',[]) if x.get('fact_id') not in seen]+cold['facts']
        cold['audit']=list(old_cold.get('audit',[]))+cold['audit']
    h3_bytes=_jbytes({'schema':'H3_DYNAMIC_TEMPLATE_V0.1','template':{'alpha':h3.t.alpha,'w0':h3.t.w0,'w1':h3.t.w1},'transient_persisted':False})
    files={'graph_hot.json':_jbytes(hot),'h3_templates.json':h3_bytes}
    if include_cold:files['cold/history.json']=_jbytes(cold)
    if runtime_state is not None:files['runtime_state.json']=_jbytes(runtime_state)
    for name,obj in (organs or {}).items():
        safe=str(name).strip().replace('..','_').strip('/')
        if not safe:raise ValueError('bad organ name')
        files[f'organs/{safe}.json']=_jbytes(obj)
    manifest={'schema':SCHEMA_COMPACT,'meta':meta,'files':sorted(files),'sha256':{k:hashlib.sha256(v).hexdigest() for k,v in files.items()},'cold_optional':include_cold}
    with ZipFile(path,'w',ZIP_DEFLATED) as z:
        z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True))
        for k,v in files.items():z.writestr(k,v)
    return manifest

def load_c4m_compact(path,*,hydrate_cold=False,with_runtime=False,with_organs=False):
    with ZipFile(path,'r') as z:
        manifest=json.loads(z.read('manifest.json'))
        if manifest.get('schema')!=SCHEMA_COMPACT:raise ValueError('not a compact C4M checkpoint')
        needed=['graph_hot.json','h3_templates.json']
        if with_runtime and 'runtime_state.json' in manifest['files']:needed.append('runtime_state.json')
        if with_organs:needed += [x for x in manifest['files'] if x.startswith('organs/') and x.endswith('.json')]
        if hydrate_cold and 'cold/history.json' in manifest['files']:needed.append('cold/history.json')
        raw={}
        for name in needed:
            b=z.read(name)
            if hashlib.sha256(b).hexdigest()!=manifest['sha256'][name]:raise ValueError(f'{name} checksum mismatch')
            raw[name]=b
    gd=json.loads(raw['graph_hot.json'])
    if hydrate_cold and 'cold/history.json' in raw:
        cold=json.loads(raw['cold/history.json'])
        gd['facts']=list(gd.get('facts',[]))+list(cold.get('facts',[]))
        gd['audit']=list(cold.get('audit',[]))
    g=C4Graph.from_dict(gd);hd=json.loads(raw['h3_templates.json'])['template'];h=DynamicBoundTrace(BinaryTraceTemplate(**hd))
    if not hydrate_cold and 'cold/history.json' in manifest['files']:
        g._unhydrated_cold_source=str(path)
    runtime_state=json.loads(raw['runtime_state.json']) if 'runtime_state.json' in raw else None
    organs={}
    if with_organs:
        for name,b in raw.items():
            if name.startswith('organs/') and name.endswith('.json'):organs[name[len('organs/'):-len('.json')]]=json.loads(b)
    if with_runtime and with_organs:return g,h,manifest,runtime_state,organs
    if with_runtime:return g,h,manifest,runtime_state
    if with_organs:return g,h,manifest,organs
    return g,h,manifest
