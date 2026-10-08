"""Event-source inquiry alignment: candidates, never an automatic ANSWER/VERIFIED claim.

The next turn is not an answer. This is EVAL-only comparison of utterance
content and simultaneously open ASK objects. Only unambiguous content overlap
proposes a link. COMMIT does not resolve the question or adopt the content.
"""
from __future__ import annotations
from .episodic_memory import features, split_episodes


def evaluate_inquiry_link(text, inquiries, source_event_id=None):
    units=split_episodes(text)
    if not units or any(x['kind']=='QUESTION' for x in units):
        return {'status':'NOT_ANSWER','candidates':[],'source_event_id':source_event_id}
    # The protocol does not interpret a quoted example as the user's answer.
    from .semantic_spine import outside_quotes
    surface=outside_quotes(text).strip()
    if not surface:
        return {'status':'NOT_ANSWER','candidates':[],'source_event_id':source_event_id}
    ff=features(surface)
    if not ff:
        return {'status':'NO_MATCH','candidates':[],'source_event_id':source_event_id}
    viable=[]
    for q in inquiries:
        if q.get('status') not in {'OPEN','BACKGROUND'}:continue
        # An ASK's surface is not a basis; only its content features supply a link.
        f=features(q.get('text',''))
        same=ff & f
        if not same:continue
        precision=len(same)/max(1,len(ff))
        recall=len(same)/max(1,len(f))
        viable.append({'question_event_id':q['event_id'], 'score':round((precision+recall)/2,5),
                       'shared_features':sorted(same),'source_event_id':source_event_id})
    viable.sort(key=lambda q:(-q['score'],q['question_event_id']))
    if not viable:
        status='NO_MATCH'
    elif len(viable)>1 and viable[0]['score']-viable[1]['score']<0.15:
        status='AMBIGUOUS'
    else:
        status='CANDIDATE'
    return {'status':status,'candidates':viable[:8],'source_event_id':source_event_id}