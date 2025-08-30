# blog/templatetags/blog_extras.py
import re
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import linebreaks

register = template.Library()


@register.filter
def clean_paragraphs(value):
    if not value:
        return ""
    s = str(value)

    # If there’s already block HTML, don’t add <p> again
    if re.search(r'</?(p|ul|ol|h\d|blockquote|pre|div)\b', s, flags=re.I):
        # Kill nested <p><p>…</p></p>
        s = re.sub(r'<p>\s*(<p\b[^>]*>)', r'\1', s, flags=re.I)
        s = re.sub(r'(</p>)\s*</p>', r'\1', s, flags=re.I)
        return mark_safe(s)

    # Plain text -> paragraphs
    return linebreaks(s)
