from django.contrib import admin
from .models import Car, News, Request

# Register your models here.
admin.site.register(Car)
admin.site.register(News)
admin.site.register(Request)