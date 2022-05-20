from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/&Ptype=<str:Ptype>&id_item=<str:id_item>/', views.product_detail, name='product_detail'),
    path('product/<str:Ptype>/', views.product_type, name='product_type'),
    path('product/add-comment', views.add_comment, name='add_comment'),
]