# portal/templatetags/portal_extras.py
from django import template
from portal.authz import is_portal_owner

register = template.Library()


@register.filter
def has_group(user, group_name: str) -> bool:
    try:
        return (
            user.is_authenticated
            and user.groups.filter(name=group_name).exists()
        )
    except Exception:
        return False


@register.filter
def is_owner(user) -> bool:
    return is_portal_owner(user)
