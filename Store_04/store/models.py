from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

from warehouse.models import Book
from customer.models import Customer

# Create your models here.


class BookItem(models.Model):
    book = models.ForeignKey(Book, related_name='bookitem_book', on_delete=models.CASCADE)
    price_in_sale = models.DecimalField(max_digits=8, decimal_places=0)
    discount = models.DecimalField(max_digits=8, decimal_places=0)

    created_by = models.ForeignKey(User, related_name='bookitem_creator', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "BookItem"

    def __str__(self):
        return f"{self.id}"


class Comment(models.Model):
    customer = models.ForeignKey(Customer, related_name='comment_customer', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='comment_book', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    comment_time = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Comment"

    def __str__(self):
        return f"{self.id}"
