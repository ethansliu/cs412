from django.contrib import admin

# Register your models here.s
from .models import *
admin.site.register(Profile)
admin.site.register(StatusMessage)
admin.site.register(Image)