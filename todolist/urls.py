from django.contrib import admin
from django.urls import path, include
from .views import home, editar, update, delete, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', home, name="home"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]    
