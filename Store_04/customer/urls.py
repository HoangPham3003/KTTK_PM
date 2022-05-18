from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('change-password/', views.change_password, name='change_password'),
]