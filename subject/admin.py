from django.contrib import admin
from .models import benefit,topic,pin_point
# ,inputs

# Register your models here.
admin.site.register(benefit)
admin.site.register(pin_point)
admin.site.register(topic)

# admin.site.register(inputs)