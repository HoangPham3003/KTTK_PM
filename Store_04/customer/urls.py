from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('change-password/', views.change_password, name='change_password'),
    path('my-orders/&order_id=<str:order_id>/', views.order_detail, name='order_detail'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('profile/', views.profile, name='profile'),
]