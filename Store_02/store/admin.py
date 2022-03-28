from django.contrib import admin
from .models import Category, Book, MobilePhone, Cloth, Laptop, Shoes

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'author', 'slug', 'price', 'created', 'updated']
    list_filter = ['author']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('code',)}


@admin.register(MobilePhone)
class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'manufacturer', 'slug', 'price', 'created', 'updated']
    list_filter = ['manufacturer']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('code',)}


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'origin', 'slug', 'price', 'created', 'updated']
    list_filter = ['origin']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('code',)}


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'manufacturer', 'slug', 'price', 'created', 'updated']
    list_filter = ['manufacturer']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('code',)}


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'manufacturer', 'slug', 'price', 'created', 'updated']
    list_filter = ['manufacturer']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('code',)}
