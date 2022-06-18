from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('register', views.index),
    path('login', views.login),
    path('users/new', views.index),
    path('users', views.user_dis)
]