from django.contrib import admin
from django.urls import path, include
from user.views import HomeView
from user import views as user_views
from design import views as design_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('todolist/', include('todolist.urls')),
    path('', HomeView.as_view(), name='home'),
    path('reports/', include('reports.urls')),
]
