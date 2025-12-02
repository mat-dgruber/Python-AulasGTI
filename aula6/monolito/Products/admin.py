from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available', 'stock', 'created_at', 'updated_at')
    list_filter = ('is_available', 'created_at', 'updated_at')
    list_editable = ('price', 'is_available', 'stock')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('name',)}
    
