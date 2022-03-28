from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart_summary'),
    path('cart-add/', views.cart_add, name='cart_add'),
    path('cart-del/', views.cart_del, name='cart_del'),
]