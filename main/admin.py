from django.contrib import admin
from .models import Flyer


@admin.register(Flyer)
class FlyerAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'event_date')  # ✅ only use existing fields
    fields = (
        'title_en', 'title_it',
        'description_en', 'description_it',
        'extra_info_en', 'extra_info_it',
        'image', 'event_date'
    )
