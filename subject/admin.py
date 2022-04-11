from django.contrib import admin
from .models import benefit,topic,pin_point

# Register your models here.
admin.site.register(benefit)
admin.site.register(pin_point)
admin.site.register(topic)