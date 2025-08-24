from django.conf import settings


def is_portal_owner(user) -> bool:
    if not user or not user.is_authenticated:
        return False
    if (
        settings.PORTAL_OWNER_USERNAME
        and user.username.lower() == settings.PORTAL_OWNER_USERNAME
    ):
        return True
    if (
        settings.PORTAL_OWNER_EMAIL
        and user.email.lower() == settings.PORTAL_OWNER_EMAIL
    ):
        return True
    return False


def in_group(user, name: str) -> bool:
    return user.is_authenticated and user.groups.filter(name=name).exists()
