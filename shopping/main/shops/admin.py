from django.contrib import admin
from .models import *
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Price)