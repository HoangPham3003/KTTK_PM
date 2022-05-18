from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

from customer.models import Customer
from store.models import BookItem, LaptopItem, ClothesItem

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
    cart = models.ForeignKey(Cart, related_name='cart_book', on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItem, related_name='cartitem_bookitem', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "CartBookItem"

    def __str__(self):
        return f"{self.id}"


class CartLaptopItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_laptop', on_delete=models.CASCADE)
    laptop_item = models.ForeignKey(LaptopItem, related_name='cartitem_laptopitem', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "CartLaptopItem"

    def __str__(self):
        return f"{self.id}"


class CartClothesItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_clothes', on_delete=models.CASCADE)
    clothes_item = models.ForeignKey(ClothesItem, related_name='cartitem_clothesitem', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "CartClothesItem"

    def __str__(self):
        return f"{self.id}"
