from django.contrib import admin
from .models import BookItem, ClothesItem, LaptopItem, CommentBook, CommentLaptop, CommentClothes

# Register your models here.


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'price_in_sale', 'discount']


@admin.register(LaptopItem)
class LaptopItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'laptop', 'price_in_sale', 'discount']


@admin.register(ClothesItem)
class ClothesItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'clothes', 'price_in_sale', 'discount']


@admin.register(CommentBook)
class CommentBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'book_item', 'comment', 'comment_time']


@admin.register(CommentLaptop)
class CommentLaptopAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'laptop_item', 'comment', 'comment_time']


@admin.register(CommentClothes)
class CommentClothesAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'clothes_item', 'comment', 'comment_time']
