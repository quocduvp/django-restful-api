from django.db import models
from menus.models import SubMenu, UUID
from producers.models import Producer
from motorbike.models import motorbike


# Create your models here.

class accessory(UUID):
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name="producer")
    title = models.CharField(max_length=200, null=False, blank=False)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    qty = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True, auto_created=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=False)

    def __str__(self):
        return self.title


#
class image(models.Model):
    accessory_id = models.ForeignKey(accessory, on_delete=models.CASCADE, related_name="images")
    source = models.ImageField(null=True, upload_to="photo/accessory")

    def __str__(self):
        return str(self.source)


class tag(models.Model):
    accessory_id = models.ForeignKey(accessory, on_delete=models.CASCADE, related_name="tags")
    sub_menu_id = models.OneToOneField(SubMenu, on_delete=models.CASCADE, related_name="category")

    def __str__(self):
        return str(self.sub_menu_id)


class require_for(models.Model):
    accessory_id = models.ForeignKey(accessory, on_delete=models.CASCADE, related_name="require_for")
    motorbike_id = models.OneToOneField(motorbike, on_delete=models.CASCADE, related_name="motobikes")

    def __str__(self):
        return str(self.motorbike_id)
