from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def clean_paragraphs(value):
    """
    Convert text with multiple line breaks into <p> tags,
    removing single newlines.
    """
    if not value:
        return ''

    # Normalize line endings
    value = value.replace('\r\n', '\n')
    value = value.replace('\r', '\n')
    paragraphs = re.split(r'\n{2,}', value)  # Split on 2+ line breaks

    html_paragraphs = [
        '<p>{}</p>'.format(
            re.sub(r'\n+', ' ', p.strip())
        )  # Remove single breaks
        for p in paragraphs if p.strip()
    ]

    return mark_safe('\n'.join(html_paragraphs))
