from django.contrib import admin
from .models import Author, Publisher, Category, Book, LaptopProducer, LaptopType, Laptop, ClothesManufacturer, ClothesStyle, Clothes

# Register your models here.


# Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'dob', 'phone']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'author', 'price', 'created', 'updated']
    list_filter = ['author']


# Laptop
@admin.register(LaptopProducer)
class LaptopProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(LaptopType)
class LaptopTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'producer', 'price', 'created', 'updated']
    list_filter = ['producer']


# Clothes
@admin.register(ClothesManufacturer)
class ClothesManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(ClothesStyle)
class ClothesStyleAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'manufacturer', 'price', 'created', 'updated']
    list_filter = ['manufacturer']

