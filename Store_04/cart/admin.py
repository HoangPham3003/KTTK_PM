from django.contrib import admin
from .models import Cart, CartBookItem

# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_cost']


@admin.register(CartBookItem)
class CartBookItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'book_item', 'quantity']
