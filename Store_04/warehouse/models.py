from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.


# Book
class Author(models.Model):
    fullname = models.CharField(max_length=255)
    dob = models.DateField(default=date.today)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='author_creator', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Book author"
        ordering = ("-fullname",)

    def __str__(self):
        return f"{self.fullname} {self.dob}"


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='publisher_creator', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Book publisher"
        ordering = ("-name",)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='category_creator', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Book category"
        ordering = ("-name",)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    number_of_page = models.DecimalField(max_digits=8, decimal_places=0)
    date_publish = models.DateTimeField(default=datetime.now)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    author = models.ForeignKey(Author, related_name='book_author', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='book_publisher', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='book_category', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='book_creator', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Books"
        ordering = ("-created",)

    def __str__(self):
        return self.title


# Laptop
class LaptopProducer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Laptop producer"

    def __str__(self):
        return self.name


class LaptopType(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Laptop type"

    def __str__(self):
        return self.name


class Laptop(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    size_screen = models.DecimalField(max_digits=8, decimal_places=0)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    producer = models.ForeignKey(LaptopProducer, related_name='laptop_producer', on_delete=models.CASCADE)
    type = models.ForeignKey(LaptopType, related_name='laptop_type', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='laptop_creator', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Laptops"
        ordering = ("-created",)

    def __str__(self):
        return self.name


# Clothes
class ClothesManufacturer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Clothes manufacturer"

    def __str__(self):
        return self.name


class ClothesStyle(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Clothes style"

    def __str__(self):
        return self.name


class Clothes(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=8, decimal_places=0)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    manufacturer = models.ForeignKey(ClothesManufacturer, related_name='clothes_manufacturer', on_delete=models.CASCADE)
    style = models.ForeignKey(ClothesStyle, related_name='clothes_style', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='clothes_creator', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Clothes"
        ordering = ("-created",)

    def __str__(self):
        return self.name