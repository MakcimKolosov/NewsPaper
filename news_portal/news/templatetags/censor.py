from django import template

register = template.Library()

@register.filter(name='censor')
def censor(text):
    # Пример замены нецензурных слов
    bad_words = ['плохое_слово1', 'плохое_слово2']
    for word in bad_words:
        text = text.replace(word, '*' * len(word))
    return text