from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('category/<str:category>/', views.category_product, name='category_product'),
    path('product/&category=<str:category>&code=<str:code>/', views.product_detail, name='product_detail'),
]
