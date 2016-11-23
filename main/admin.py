from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug')
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'price', 'category', 'photo')
    