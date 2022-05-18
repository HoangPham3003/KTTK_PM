from django.contrib import admin
from .models import BookItem, Comment, ClothesItem, LaptopItem

# Register your models here.


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'price_in_sale', 'discount']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'book', 'comment', 'comment_time']


@admin.register(LaptopItem)
class LaptopItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'laptop', 'price_in_sale', 'discount']


@admin.register(ClothesItem)
class ClothesItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'clothes', 'price_in_sale', 'discount']
