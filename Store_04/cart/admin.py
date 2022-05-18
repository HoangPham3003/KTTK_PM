from django.contrib import admin
from .models import Cart, CartBookItem, CartLaptopItem, CartClothesItem

# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_cost']


@admin.register(CartBookItem)
class CartBookItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'book_item', 'quantity']


@admin.register(CartLaptopItem)
class CartLaptopItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'laptop_item', 'quantity']


@admin.register(CartClothesItem)
class CartClothesItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'clothes_item', 'quantity']
