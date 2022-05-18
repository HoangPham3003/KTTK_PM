from django.contrib import admin
from .models import BookItem, Comment

# Register your models here.


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ['book', 'price_in_sale', 'discount']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['customer', 'book', 'comment', 'comment_time']
