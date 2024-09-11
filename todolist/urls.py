from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create/', CriarMetaView.as_view(), name='create-meta'),
    path('editar/<int:id>', EditarMetaView.as_view(), name='editar'),
    path('delete/<int:id>', DeletarMetaView.as_view(), name='delete'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]    
