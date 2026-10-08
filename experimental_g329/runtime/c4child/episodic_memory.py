"""G328: append-only transport episode index and source-bounded recall, never WORLD COMMIT.

An input transport message is *not* a teaching transaction. Numbered questions
and embedded quotes are retained as episodes with provenance. Memory retrieval
only reports earlier witnessed messages, and never treats questions/examples as
independent physical observations.
"""
from __future__ import annotations
import re
from dataclasses import dataclass, asdict
import math
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



def outside_direct_questions(text:str)->str:
    """Mask quotations to distinguish asked questions from reported questions."""
    buf=[];stack=[];pair={'«':'»','“':'”','"':'"'}
    for ch in str(text):
        if stack and ch==stack[-1]:
            stack.pop();buf.append(' ');continue
        if ch in pair:
            stack.append(pair[ch]);buf.append(' ');continue
        buf.append(' ' if stack else ch)
    return ''.join(buf)

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
            has_question='?' in outside_direct_questions(part)
            out.append({'number':n,'line':line_idx+1,'text':part,'kind':'QUESTION' if has_question else 'TEXT',
                        'scope':'UNCOMMITTED_SURFACE'})
    return out

def is_query_batch(episodes:List[dict])->bool:
    questions=sum(x['kind']=='QUESTION' for x in episodes)
    # Three+ interrogatives form a batch; numbered list can also include questions
    # with missing terminal '?' or nested quoted question punctuation.
    # Multiple direct interrogative acts are a single read-only inquiry transaction.
    # No topic-specific answer key and no arbitrary 3/5-question safety threshold.
    return questions>1

_MEMORY_CUES = re.compile(r'\b(?:помнишь|вспомни|помнит|помню|вспомина|раньше|прежде|прошл[а-я]*|стар[а-я]*\s+вопрос|до\s+этого|мы\s+(?:говорили|обсуждали)|я\s+(?:говорил|спрашивал|рассказывал)|ты\s+(?:говорила|спрашивала|отвечала|писала|задала)|из\s+нашего\s+разговора|еще\s+открыты|остались\s+без\s+ответа)\b',re.I)

def is_memory_query(text:str)->bool:
    return '?' in text and bool(_MEMORY_CUES.search(text))

def index_event(event_id:str,order:int,text:str)->dict:
    ep=split_episodes(text)
    return {'event_id':event_id,'external_order':int(order),'episodes':ep,
            'scope':'QUERY_BATCH' if is_query_batch(ep) else 'UNCOMMITTED_TRANSPORT',
            'source_kind':'USER_MESSAGE','epistemic':'SOURCE_SAID_ONLY'}

def retrieve(question:str,index:dict,current_event_id=None,limit:int=2)->List[dict]:
    """Source-bounded old-event retrieval with inverse-frequency ranking.

    A single distinctive named entity can identify an actual witnessed event.
    Similarity is never evidence the event's *content* happened in the world.
    """
    query=features(question)
    if not query:return []
    asks_about_questions=bool(re.search(r'\b(?:вопрос[а-я]*|спрашивал[а-я]*|спросил[а-я]*|задавал[а-я]*|задал[а-я]*)\b',question.casefold()))
    asks_c4_reply=bool(re.search(r'\b(?:ты|тво[а-я]*|сво[а-я]*)\b',question.casefold()) and
                         re.search(r'\b(?:сказал[а-я]*|говорил[а-я]*|ответил[а-я]*|писал[а-я]*)\b',question.casefold()))
    docs=[]
    for item in index.values():
        if item.get('event_id')==current_event_id:continue
        for ep in item.get('episodes',[]):
            if ep.get('kind')=='QUESTION' and not asks_about_questions:continue
            if item.get('source_kind')=='C4_REPLY' and not asks_c4_reply:continue
            docs.append((item,ep,features(ep.get('text',''))))
    if not docs:return []
    df={w:sum(w in fs for _,_,fs in docs) for w in query}
    idf={w:math.log1p((len(docs)+1)/(1+df[w])) for w in query}
    denom=sum(idf.values())
    found=[]
    for item,ep,f in docs:
        shared=query & f
        if not shared:continue
        score=sum(idf[w] for w in shared)/max(1e-9,denom)
        # A match whose source span contains many unrelated concepts has
        # lower retrieval priority, but is still valid as a transcript hit.
        specificity=(1+len(shared))/(1+max(len(f),len(shared)))
        score*=0.75+0.25*specificity
        if item.get('scope')=='QUERY_BATCH' and not asks_about_questions:score*=.80
        found.append({'event_id':item['event_id'],'external_order':item.get('external_order',0),
                      'line':ep.get('line',0),'text':ep.get('text',''),'source_kind':item.get('source_kind'),
                      'episode_kind':ep.get('kind'),'score':round(score,4), 'shared':sorted(shared)})
    found.sort(key=lambda z:(z['score'],z['external_order']),reverse=True)
    seen=set();unique=[]
    for row in found:
        key=(row['event_id'],row['text'])
        if key in seen:continue
        seen.add(key);unique.append(row)
        if len(unique)>=limit:break
    return unique


def is_inquiry_query(query:str)->bool:
    """Structural discourse query over C4's own previously spoken ASK events."""
    outside=outside_direct_questions(query).casefold().replace('ё','е')
    if '?' not in outside:return False
    question_act=bool(re.search(r'\b(?:вопрос[а-я]*|спрашивал[а-я]*|спросил[а-я]*|задавал[а-я]*|задал[а-я]*)\b',outside))
    self_ref=bool(re.search(r'\b(?:ты|тебя|тво[ияе][а-я]*|сво[ияе][а-я]*|сама|сам[а-я]*)\b',outside))
    return question_act and self_ref


def attributed_inquiry_recall(query:str,inquiries)->dict|None:
    """Query the witnessed C4 ASK ledger, not general lexical facts.

    A concept-level interrogative referring to C4's past questions acts as a
    query over typed ASK events. Only its surface intent is recognized; question
    content and status are retrieved from real stored events.
    """
    if not is_inquiry_query(query):return None
    outside=outside_direct_questions(query).casefold().replace('ё','е')
    items=[q for q in inquiries if isinstance(q,dict) and q.get('event_id') and q.get('text')]
    if not items:return None
    # Filter by meaningful topic overlap; absent a topic this is an event-type
    # query and can enumerate open/inactive inquiries without word matching.
    # Functional terms indicate a query about discourse, not its content topic.
    # This lexical grammar is open-domain; no specific entity/content is special.
    functional=re.compile(r'^(?:вопрос|ответ|спраш|спрос|зада|задал|помн|вспом|сво|тво|мо[йие]|сам|стар|прошл|раньш|остал|неотвеч|каки|како|скольк|три|два|один|перв|втор|трет)',re.I)
    topic={w for w in features(query) if not functional.match(w)}
    matches=[]
    for q in items:
        f=features(q['text']);common=topic & f
        if topic and not common:continue
        if topic and len(common)*2 < len(topic):continue
        matches.append(q)
    if not matches:return None
    # Explicitly asking about still-open items filters by the actual state.
    open_only=bool(re.search(r'\b(?:открыт[а-я]*|без\s+ответ[а-я]*|неотвеченн[а-я]*|остал[а-я]*)\b',outside))
    if open_only:matches=[q for q in matches if q.get('status') in ('OPEN','BACKGROUND')]
    if not matches:return None
    ordered=sorted(matches,key=lambda q:(int(q.get('created_step',0)),str(q['event_id'])))
    lines=[f'«{q["text"][:180]}» — {q.get("status","UNKNOWN")}' for q in ordered[-12:]]
    refs=[{'event_id':q['event_id'],'text':q['text'],'episode_kind':'QUESTION',
           'source_kind':'C4_ASK', 'status':q.get('status','UNKNOWN')} for q in ordered[-12:]]
    return {'status':'RETRIEVED_INQUIRIES',
            'reply':'У меня есть записи собственных вопросов:\n'+'\n'.join(lines)+
                    '\nЭто мои прежние вопросы, а не доказательство ответов.',
            'refs':refs}


def answer_memory_query(query:str,index:dict,current_event_id=None,inquiries=())->dict:
    own=attributed_inquiry_recall(query,inquiries)
    if own is not None:return own
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


def answer_batch(episodes:List[dict],index:dict,current_event_id=None,max_items:int=32,inquiries=())->dict:
    lines=[];refs=[];nq=0;found=0
    for ep in episodes:
        if ep.get('kind')!='QUESTION':continue
        nq+=1
        if nq>max_items:break
        q=ep['text']
        num=ep.get('number') or nq
        if is_memory_query(q):
            r=answer_memory_query(q,index,current_event_id,inquiries=inquiries)
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