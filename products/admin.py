from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Subcategories)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

