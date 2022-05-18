from django.contrib import admin
from .models import Order, OrderItem, Shipment, Payment

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'date_time_created', 'order_completed']
    list_filter = ['order_completed', 'customer']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_type', 'item_id']
    list_filter = ['order__order_completed', 'order__id']


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['order', 'address', 'shipment_price', 'shipment_completed']
    list_filter = ['shipment_completed', 'order__id']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'type', 'total_cost', 'payment_completed']
    list_filter = ['payment_completed', 'order__id']

