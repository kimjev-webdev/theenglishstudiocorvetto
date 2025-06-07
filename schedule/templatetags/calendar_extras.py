from django import template
register = template.Library()


@register.filter
def dict_key(dict_data, key):
    return dict_data.get(key, [])
