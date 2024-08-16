from django.contrib import admin
from django.urls import path, include
from .views import home, editar, update, delete

urlpatterns = [
    path('', home, name="home"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]    
