from django.db import models
import uuid


# Create your models here.

class UUID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Menu(UUID):
    menu_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.menu_name)


class SubMenu(UUID):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="sub_menu")
    sub_menu_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.sub_menu_name

