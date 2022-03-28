from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='book_creator', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Books"
        ordering = ("-created",)

    def __str__(self):
        return self.title


class MobilePhone(models.Model):
    category = models.ForeignKey(Category, related_name='mobilephone', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='mobilephone_creator', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Mobile phones"
        ordering = ("-created",)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    category = models.ForeignKey(Category, related_name='cloth', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='cloth_creator', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Clothes"
        ordering = ("-created",)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    category = models.ForeignKey(Category, related_name='laptop', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='laptop_creator', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Laptops"
        ordering = ("-created",)

    def __str__(self):
        return self.name


class Shoes(models.Model):
    category = models.ForeignKey(Category, related_name='shoes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='shoes_creator', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Shoes"
        ordering = ("-created",)

    def __str__(self):
        return self.name





