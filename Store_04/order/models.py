from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

from cart.models import Cart
from customer.models import Customer


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='order_customer', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='order_cart', on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order_completed = models.BooleanField(default=False)  # order was finished or not

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Order"

    def __str__(self):
        return f"{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitem_order', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=255)
    item_id = models.DecimalField(max_digits=8, decimal_places=0)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "OrderItem"

    def __str__(self):
        return f"{self.id}"


class Shipment(models.Model):
    order = models.ForeignKey(Order, related_name='shipment_order', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    shipment_price = models.DecimalField(max_digits=8, decimal_places=0)
    shipment_completed = models.BooleanField(default=False)  # shipment was finished or not

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Shipment"

    def __str__(self):
        return f"{self.id}"


class Payment(models.Model):
    order = models.ForeignKey(Order, related_name='payment_order', on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    total_cost = models.DecimalField(max_digits=8, decimal_places=0)
    payment_completed = models.BooleanField(default=False)  # payment was finished or not

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Payment"

    def __str__(self):
        return f"{self.id}"
