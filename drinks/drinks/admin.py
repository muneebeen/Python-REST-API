from django.contrib import admin
from .models import Drink

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')

admin.site.register(Drink, ProductAdmin)