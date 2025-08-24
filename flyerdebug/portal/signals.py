from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

FEATURE_APPS = {
    "BLOG": "blog",
    "SCHEDULE": "schedule",
    "FLYERS": "flyers",
}


@receiver(post_migrate)
def ensure_feature_groups(sender, **kwargs):
    for group_name, app_label in FEATURE_APPS.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        cts = ContentType.objects.filter(app_label=app_label)
        perms = Permission.objects.filter(content_type__in=cts)
        group.permissions.set(perms)
