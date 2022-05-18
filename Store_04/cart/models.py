from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

from customer.models import Customer
from store.models import BookItem

# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(Customer, related_name='cart_customer', on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=8, decimal_places=0)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Cart"

    def __str__(self):
        return f"{self.id}"


class CartBookItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cartitem_cart', on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItem, related_name='cartitem_bookitem', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "CartBookItem"

    def __str__(self):
        return f"{self.id}"
