"""G328: append-only transport episode index and source-bounded recall, never WORLD COMMIT.

An input transport message is *not* a teaching transaction. Numbered questions
and embedded quotes are retained as episodes with provenance. Memory retrieval
only reports earlier witnessed messages, and never treats questions/examples as
independent physical observations.
"""
from __future__ import annotations
import re
from dataclasses import dataclass, asdict
from typing import Dict, List

_WORD = re.compile(r'[\wА-Яа-яЁё-]{3,}', re.U)
_NUMBERED = re.compile(r'^\s*(?:\*\*\s*)?(\d{1,3})\s*[.)]\s*(?:\*\*)?\s*(.*?)\s*$',re.S)
_STOP = frozenset('''а и или но не да ли как кто что это та тот эта вот где когда зачем почему сколько какие какой какая какое каких котором с со от до для при про еще уже было был была были будем будет могу можешь можно нужно тогда том там здесь вот вы мне меня я мы ты тебя себе себе твоих своих своих ранее раньше прошлом прошлых прошлый прошлую наш нашему нашего наших вопрос вопросы вопросе ответ ответил отвечал вспомни помнишь помни знала знаешь точно сам сама самой самих говорит говорил говорил говорили сказала сказал слова слово фраза случае если после перед сейчас теперь опять уже тогда этом этого этой истории разговоре разговаривали говорили думаешь было потом когда еще раз тем как можешь можешь ли можем ли обязательно ли это это было что'''.split())
_ENDINGS=('иями','ыми','ими','иями','ание','ение','ного','ному','евой','овых','иями','аться','ится','илась','ились','ать','ить','ять','ого','ему','ами','ями','иях','ениях','ешь','али','ала','ила','али','ото','ыми','ыми','ной','ого','ыми','ова','ыми','ая','ое','ое','ые','ов','ев','ам','ям','ах','ях','ой','ий','ый','ую','ом','ем','ей','ил','ла','ли','на','у','ю','а','я','ы','и','е')

def stem(w:str)->str:
    w=w.casefold().replace('ё','е').strip('-')
    for end in _ENDINGS:
        if len(w)>len(end)+2 and w.endswith(end):return w[:-len(end)]
    return w

def features(text:str)->set:
    return {stem(x) for x in _WORD.findall(str(text)) if x.casefold() not in _STOP and len(x)>3}

def split_episodes(text:str)->List[dict]:
    """Line/numbered spans, then punctuation outside nested quotations.

    Always preserve original text; spans are descriptive index entries, not
    independently admitted claims.
    """
    out=[];paragraphs=str(text).splitlines()
    for line_idx,line in enumerate(paragraphs):
        line=line.strip()
        if not line:continue
        m=_NUMBERED.match(line);n=int(m.group(1)) if m else None
        if m:line=m.group(2).strip()
        # In a numbered item, retain composite sentences as one task context.
        parts=[line] if n is not None else []
        if n is None:
            stack=[];start=0;pair={'«':'»','“':'”','"':'"'}
            for idx,ch in enumerate(line):
                if stack and ch==stack[-1]:stack.pop()
                elif ch in pair:stack.append(pair[ch])
                if not stack and ch in '.!?' and (idx+1==len(line) or line[idx+1].isspace()):
                    parts.append(line[start:idx+1].strip());start=idx+1
            if start<len(line):parts.append(line[start:].strip())
        for part in parts:
            if not part:continue
            # Mark interrogative even when an item contains narrated quotes and
            # several punctuation marks. Doesn't assert its premises.
            has_question='?' in part
            out.append({'number':n,'line':line_idx+1,'text':part,'kind':'QUESTION' if has_question else 'TEXT',
                        'scope':'UNCOMMITTED_SURFACE'})
    return out

def is_query_batch(episodes:List[dict])->bool:
    questions=sum(x['kind']=='QUESTION' for x in episodes)
    # Three+ interrogatives form a batch; numbered list can also include questions
    # with missing terminal '?' or nested quoted question punctuation.
    return questions>=3 or (len(episodes)>=5 and sum(x['number'] is not None for x in episodes)>=3 and questions>=2)

_MEMORY_CUES = re.compile(r'\b(?:помнишь|вспомни|помнит|помню|вспомина|раньше|прежде|прошл[а-я]*|стар[а-я]*\s+вопрос|до\s+этого|мы\s+(?:говорили|обсуждали)|я\s+(?:говорил|спрашивал|рассказывал)|ты\s+(?:говорила|спрашивала|отвечала|писала|задала)|из\s+нашего\s+разговора|еще\s+открыты|остались\s+без\s+ответа)\b',re.I)

def is_memory_query(text:str)->bool:
    return '?' in text and bool(_MEMORY_CUES.search(text))

def index_event(event_id:str,order:int,text:str)->dict:
    ep=split_episodes(text)
    return {'event_id':event_id,'external_order':int(order),'episodes':ep,
            'scope':'QUERY_BATCH' if is_query_batch(ep) else 'UNCOMMITTED_TRANSPORT',
            'source_kind':'USER_MESSAGE','epistemic':'SOURCE_SAID_ONLY'}

def retrieve(question:str,index:dict,current_event_id=None,limit:int=2)->List[dict]:
    """Evidence-only lexical candidate retrieval, not semantic entailment.

    Insist on two independent content feature intersections to prevent the
    'буква И' kind of unrestricted subject-word top hits. Skips current event
    so repeating a question cannot manufacture a memory of a previous turn.
    """
    query=features(question)
    if len(query)<2:return []
    # A past *question about* an alleged event is evidence the question was
    # asked, not that the alleged event took place. Only queries explicitly
    # asking about earlier questions may prefer interrogative records.
    asks_about_questions=bool(re.search(r'\b(?:вопрос[а-я]*|спрашивал[а-я]*|спросил[а-я]*|задавал[а-я]*|задал[а-я]*)\b',question.casefold()))
    found=[]
    for item in index.values():
        if item.get('event_id')==current_event_id:continue
        for ep in item.get('episodes',[]):
            text=ep.get('text','');f=features(text)
            shared=query & f
            if len(shared)<2:continue
            score=2*len(shared)/max(1,len(query)+len(f))
            if ep.get('kind')=='QUESTION':
                if not asks_about_questions:continue
                score*=1.03
            if item.get('scope')=='QUERY_BATCH' and not asks_about_questions:
                score*=.80
            if score<0.21:continue
            found.append({'event_id':item['event_id'],'external_order':item.get('external_order',0),
                          'line':ep.get('line',0),'text':text,'source_kind':item.get('source_kind'),
                          'episode_kind':ep.get('kind'), 'score':round(score,4), 'shared':sorted(shared)})
    found.sort(key=lambda z:(z['score'],z['external_order']),reverse=True)
    dedup=set();unique=[]
    for p in found:
        k=(p['event_id'],p['text'])
        if k in dedup:continue
        dedup.add(k);unique.append(p)
        if len(unique)>=limit:break
    return unique

def answer_memory_query(query:str,index:dict,current_event_id=None)->dict:
    matches=retrieve(query,index,current_event_id=current_event_id)
    if not matches:
        return {'status':'NO_EVIDENCE','reply':'Не нахожу достаточно похожего более раннего сообщения. Я не буду придумывать воспоминание.', 'refs':[]}
    top=matches[0]
    # A retrieved QUESTION is a prior question, NOT a past confirmed answer.
    kind='вопрос' if top['episode_kind']=='QUESTION' else 'фрагмент'
    body=top['text'][:230]
    msg=f'В сохранённом сообщении ранее был {kind}: «{body}» Это запись текста, а не доказательство описанных событий.'
    if len(matches)>1 and matches[1]['score']>=top['score']-.1:
        msg+=' Нашлось несколько похожих мест, поэтому связь может быть неоднозначной.'
    return {'status':'RETRIEVED_TEXT','reply':msg,'refs':matches}


def answer_batch(episodes:List[dict],index:dict,current_event_id=None,max_items:int=32)->dict:
    lines=[];refs=[];nq=0;found=0
    for ep in episodes:
        if ep.get('kind')!='QUESTION':continue
        nq+=1
        if nq>max_items:break
        q=ep['text']
        num=ep.get('number') or nq
        if is_memory_query(q):
            r=answer_memory_query(q,index,current_event_id)
            refs.extend(r['refs'])
            if r['refs']:
                found+=1
                # Exact historical snippet rather than a claimed interpretation.
                sample=r['refs'][0]['text'][:150]
                lines.append(f'{num}. В старых сообщениях: «{sample}» (запись, не подтверждение события).')
            else:lines.append(f'{num}. Нет надёжно найденной старой записи.')
        else:
            lines.append(f'{num}. Это отдельный вопрос. Я пока не могу надёжно связать его с нужной ситуацией; не буду подменять ответ словами из базы.')
    if len(episodes)>max_items:lines.append('Часть вопросов осталась не разобрана.')
    return {'status':'READ_ONLY_BATCH','reply':'Разобрала сообщение как отдельные вопросы. Ответы по истории без выдуманных воспоминаний:\n'+'\n'.join(lines),
            'refs':refs,'question_count':nq,'grounded_hits':found}