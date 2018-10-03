from django.db import models
from menus.models import UUID
from accessories.models import accessory
from django.contrib.auth.models import User
# Create your models here.
class Carts(UUID):
    accessory_id = models.ForeignKey(accessory, on_delete=models.CASCADE, related_name="carts")
    qty = models.IntegerField(default=0, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    updated_at = models.DateTimeField(auto_now=True, auto_created=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=False)

    def __str__(self):
        return str(self.accessory_id)