from django.shortcuts import render, aget_object_or_404
from django.http import HttpResponse
from .models import MonthlyData, YearlyData, Report
import csv
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# View para exibir dados mensais e gerar um relatório
def generate_monthly_report(request, year, month):
    data = aget_object_or_404(MonthlyData, year=year, month=month)
    # adicionar lógica de cálculo ou agregação
    return render(request, 'report/monthly_report.html', {'data': data})

# View para gerar e exportar relatório em CSV
def export_report_csv(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f"attachment; filename='{report.report_name}.csv'"

    writer = csv.writer(response)
    writer.writerow(['Month', 'Year', 'Value'])
    monthly_data = MonthlyData.objects.all()

    for data in monthly_data:
        writer.writerow([data.month, data.year, data.data_value])

    return response

# View para gerar e exportar relatório em PDF
def export_report_pdf(request, report_id):
    report = aget_object_or_404(Report, id=report_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f"attachment; filename='{report.report_name}.pdf'"

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, f"Relatório: {report.report_name}")
    p.drawString(100, 730, f"Data de criação: {report.created_at.strtime('%Y-%m-%d')}")

    p.drawString(100, 700, "Dados Mensais:")
    y = 680
    monthly_data = MonthlyData.objects.all()

    for data in monthly_data:
        p.drawString(100, y, f"{data.month}/{data.year} - {data.data_value}")
        y -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    return  HttpResponse(buffer, content_type='application/pdf')

# View para listar todos os relatórios disponíveis
def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report/report_list.html', {'reports': reports})
