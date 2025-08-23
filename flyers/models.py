# flyers/models.py
from django.db import models
from django.utils import timezone


class Flyer(models.Model):
    # Titles
    title_en = models.CharField(max_length=200)
    title_it = models.CharField(max_length=200, blank=True, default="")

    # Descriptions (rich text in forms; plain TextField in DB)
    description_en = models.TextField(blank=True, default="")
    description_it = models.TextField(blank=True, default="")

    # Extra info lines (small blurb shown in modal)
    extra_info_en = models.CharField(max_length=255, blank=True, default="")
    extra_info_it = models.CharField(max_length=255, blank=True, default="")

    # Image (Cloudinary-backed by your DEFAULT_FILE_STORAGE)
    # default="" avoids interactive default prompts when adding to
    # existing rows
    image = models.ImageField(upload_to="flyers/", blank=True, default="")

    # Event date (nullable so migrations won’t fail on existing rows)
    event_date = models.DateField(blank=True, null=True)

    # Manual ordering for homepage/portal drag & drop
    sort_order = models.PositiveIntegerField(default=0, db_index=True)

    # Audit
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ["sort_order", "event_date", "id"]

    def __str__(self):
        return self.title_en or self.title_it or f"Flyer #{self.pk}"
