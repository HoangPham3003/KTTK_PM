from django.contrib import admin
from .models import Account, Address, Fullname, Customer

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['number_of_house', 'street', 'district', 'city', 'country']


@admin.register(Fullname)
class FullnameAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'midname', 'firstname']


@admin.register(Customer)
class FullnameAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'dob', 'phone']
