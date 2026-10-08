"""Conservative provenance self-query resolver. EVAL-only, no self-evidence."""
import re

_WHY=re.compile(r'\b(?:почему|на\s+каком\s+основании|откуда)\b',re.I)
_SELF=re.compile(r'\b(?:ты|тебя|твой|твоя|твоё|твое|твоём|твоем|твои|тебе|у\s+тебя)\b',re.I)
_JUSTIFY=re.compile(r'\b(?:уверен\w*|знаешь|считаешь|говоришь|утверждаешь|думаешь|ответ\w*|основан\w*|доказател\w*|вывод\w*)\b',re.I)
_DISTINGUISH=re.compile(r'\b(?:знаешь|видел\w*|наблюдал\w*|предполагаешь|предположени\w*|действительно|основани\w*)\b',re.I)

def inspect_question(text, history, events):
    """Return candidate narrative grounded in known channel metadata or None.

    Asks why THIS system is confident; distinguish its own report from independent
    world verification. Do not claim even an admitted legacy fact as observation.
    """
    t=str(text).strip()
    if not _SELF.search(t):return None
    history=list(history)
    prev=next((r for r in reversed(history) if r.get('speaker')=='C4'),None)
    if _WHY.search(t) and _JUSTIFY.search(t):
        if prev is None:
            return {'kind':'SOURCE_SELF_AUDIT','reply':'У меня пока нет собственного предыдущего ответа для проверки его оснований.'}
        reason=prev.get('reason','не указан')
        return {'kind':'SOURCE_SELF_AUDIT','reply':f'Мой предыдущий ответ — мой вывод, а не независимое наблюдение. Записанная причина ответа: {reason}. Без проверки источников я не могу утверждать, что он достоверен.'}
    # A self-source-discrimination query rather than a question about a world object.
    if ('?' in t and len(_DISTINGUISH.findall(t))>=2):
        channels={str(e.get('channel')) for e in (events or {}).values()}
        if channels<= {'CHAT_TEXT'}:
            reply='Я получила текстовые сообщения, но в этой записи нет независимого сенсорного подтверждения описанных ими событий. Мои интерпретации — гипотезы, а не наблюдения мира.'
        else:
            reply='Я различаю сообщения, гипотезы и зарегистрированные внешние события, но подтверждение конкретного факта требует проверки его источника и receipt.'
        return {'kind':'SOURCE_SELF_AUDIT','reply':reply}
    return None