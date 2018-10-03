from django.db import models
from menus.models import UUID
from django.contrib.auth.models import User
from accessories.models import accessory


# Create your models here.
class Orders(UUID):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    is_delivery = models.BooleanField(default=False, null=False)
    is_pay = models.BooleanField(default=False, null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=False)

    def __str__(self):
        return str(self.id)


class OrderItem(UUID):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order_items")
    accessory_id = models.ForeignKey(accessory, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=False)

    def __str__(self):
        return str(self.id)
