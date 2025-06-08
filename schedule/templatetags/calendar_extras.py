from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def clean_paragraphs(value):
    # Normalize line endings
    value = value.replace('\r\n', '\n').replace('\r', '\n')

    # Split into paragraphs by two or more line breaks
    paragraphs = re.split(r'\n{2,}', value)

    # Wrap each paragraph in <p> tags and remove single line breaks
    html_paragraphs = [
        '<p>{}</p>'.format(re.sub(r'\n+', ' ', p.strip()))
        for p in paragraphs if p.strip()
    ]

    return mark_safe('\n'.join(html_paragraphs))
