from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [Order.__str__,  'total_cost', 'order_completed']
    list_filter = ['order_completed', 'email']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'category', 'item_code', 'price']
    list_filter = ['order__order_completed', 'order', 'order__email']
