from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order_checkout, name='order_checkout'),
    path('checkout/', views.order_checkout, name='order_checkout'),
    path('success/', views.order_success, name='order_success'),
]