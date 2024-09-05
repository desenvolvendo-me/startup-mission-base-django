from django.urls import path
from . import views
from .views import DashboardView, generate_monthly_report

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('monthly-report/', generate_monthly_report, name='generate_monthly_report'),
]
