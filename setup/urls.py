from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from user.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('todolist/', include('todolist.urls')),
    path('', HomeView.as_view(), name='home'),
    path('', include('user.urls'))
]
