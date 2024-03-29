from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.user_logout, name='logout'),
]