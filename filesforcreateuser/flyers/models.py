from django.db import models
from cloudinary.models import CloudinaryField   


class Flyer(models.Model):
    title_en = models.CharField(max_length=100)
    title_it = models.CharField(max_length=100)
    description_en = models.TextField()
    description_it = models.TextField()
    extra_info_en = models.CharField(max_length=200, blank=True)
    extra_info_it = models.CharField(max_length=200, blank=True)
    image = CloudinaryField('image')
    event_date = models.DateField()

    def __str__(self):
        return f"{self.title_en} / {self.title_it}"
