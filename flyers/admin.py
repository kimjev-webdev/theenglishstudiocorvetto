# flyers/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Flyer


@admin.register(Flyer)
class FlyerAdmin(admin.ModelAdmin):
    # Small image preview (safe even if image field is missing/empty)
    def thumb(self, obj):
        img = getattr(obj, "image", None)
        if img:
            try:
                return format_html(
                    (
                        '<img src="{}" '
                        'style="height:48px;width:auto;border-radius:4px;" />'
                    ),
                    img.url
                )
            except Exception:
                pass
        return "—"
    thumb.short_description = "Preview"

    def get_list_display(self, request):
        cols = ["thumb", "id"]
        if hasattr(Flyer, "sort_order"):
            cols.append("sort_order")
        if hasattr(Flyer, "title_en"):
            cols.append("title_en")
        elif hasattr(Flyer, "title_it"):
            cols.append("title_it")
        if hasattr(Flyer, "event_date"):
            cols.append("event_date")
        return cols

    def get_ordering(self, request):
        if hasattr(Flyer, "sort_order") and hasattr(Flyer, "event_date"):
            return ("sort_order", "event_date", "id")
        if hasattr(Flyer, "sort_order"):
            return ("sort_order", "id")
        return ("id",)

    def get_list_filter(self, request):
        filters = []
        if hasattr(Flyer, "event_date"):
            filters.append("event_date")
        return filters

    def get_search_fields(self, request):
        fields = []
        if hasattr(Flyer, "title_en"):
            fields.append("title_en")
        if hasattr(Flyer, "title_it"):
            fields.append("title_it")
        if hasattr(Flyer, "description_en"):
            fields.append("description_en")
        if hasattr(Flyer, "description_it"):
            fields.append("description_it")
        return tuple(fields)

    def get_readonly_fields(self, request, obj=None):
        ro = []
        if hasattr(Flyer, "created_at"):
            ro.append("created_at")
        return tuple(ro)
