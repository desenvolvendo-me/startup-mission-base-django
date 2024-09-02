from django.contrib import admin
from django.urls import path, include
from user import views
from design import views
from user.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include('user.urls'))
]
