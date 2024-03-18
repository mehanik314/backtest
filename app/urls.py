from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mymodels/', views.User_Data, name="Data"),
    path('/', views.Hello, name="Data"),
]
