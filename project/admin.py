from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Closet)
admin.site.register(Category)
admin.site.register(Clothes)
admin.site.register(Outfit)
admin.site.register(Sell)