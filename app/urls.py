from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mymodels/', views.User_Data, name="Data"),
    path('projects/', views.Projects_Data, name="Data"),
    path('Tasks/', views.Get_Tasks, name="Data"),

]
