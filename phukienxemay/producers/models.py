from django.db import models
from menus.models import UUID


# Create your models here.
class Producer(UUID):
    name = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(null=True, upload_to="photo")
    descriptions = models.TextField()
    updated_at = models.DateTimeField(auto_now=True, auto_created=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=False)

    def __str__(self):
        return self.name
