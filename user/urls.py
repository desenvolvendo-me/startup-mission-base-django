from django.urls import path
from .views import signup, custom_login_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', custom_login_view, name='login'),
]
