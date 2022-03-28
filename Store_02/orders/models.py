from django.db import models
from django.conf import settings
from decimal import Decimal
from store.models import Category, Book, MobilePhone, Cloth, Laptop, Shoes
from datetime import datetime, tzinfo, timedelta
import pytz

# Create your models here.

categories = {'Books': Book, 'MobilePhones': MobilePhone, 'Clothes': Cloth, 'Laptops': Laptop, 'Shoes': Shoes}


class Order(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)
    total_cost = models.DecimalField(max_digits=8, decimal_places=0)
    order_completed = models.BooleanField(default=False)  # order was finished or not

    class Meta:
        verbose_name_plural = "Order"
        ordering = ('-created',)

    def __str__(self):
        type_month_1 = [1, 3, 5, 7, 8, 10, 12]
        type_month_2 = [2]
        type_month_3 = [4, 6, 9, 11]

        year = self.created.year
        month = self.created.month
        date = self.created.day
        hour = self.created.hour + 7
        if hour >= 24:
            hour = 0
            date += 1
            if month in type_month_1:
                if date > 31:
                    date = 1
                    month += 1
            elif month in type_month_2:
                if date > 29:
                    date = 1
                    month += 1
            elif month in type_month_3:
                if date > 30:
                    date = 1
                    month += 1
            if month > 12:
                month = 1
                year += 1

        minute = self.created.minute
        second = self.created.second
        date_time = f"{year}/{month}/{date} {hour}:{minute}:{second}"
        return str(str(self.email) + " - " + date_time)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    item_code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        verbose_name_plural = "OrderItem"

    def __str__(self):
        return str(self.id)

