from django.contrib import admin
from .models import accessory, image, tag

# Register your models here.
admin.site.register(accessory)
admin.site.register(image)
admin.site.register(tag)
