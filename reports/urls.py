from django.urls import path
from . import views

urlpatterns = [
    path('report/monthly/<int:year>/<int:month>/', views.generate_monthly_report, name='generate_monthly_report'),
    path('report/export/csv/<int:report_id>/', views.export_report_csv, name='export_report_csv'),
    path('report/export/pdf/<int:report_id>/', views.export_report_pdf, name='export_report_pdf'),
    path('report/list/', views.report_list, name='report_list'),
]
