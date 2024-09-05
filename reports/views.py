from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import csv

from todolist.models import Meta, Task


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Exemplo de parametrização simples com contagem de metas e tarefas
        context['total_metas'] = Meta.objects.count()
        context['total_tasks'] = Task.objects.count()

        # Relatórios específicos
        context['metas_executando'] = Meta.objects.filter(status='executando').count()
        context['tasks_concluidas'] = Task.objects.filter(status='concluido').count()

        return context


# Exemplo básico de função que gera um relatório mensal
def generate_monthly_report(request):
    # Gerar alguns dados fictícios para o relatório
    data = [
        {'date': '2024-09-01', 'description': 'Vendas', 'amount': 1000},
        {'date': '2024-09-02', 'description': 'Serviços', 'amount': 1500},
        {'date': '2024-09-03', 'description': 'Consultoria', 'amount': 2000},
    ]

    # Definir o nome do arquivo de relatório
    filename = f"monthly_report_{datetime.now().strftime('%Y_%m')}.csv"

    # Definir o tipo de resposta para CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Criar o escritor CSV
    writer = csv.writer(response)
    writer.writerow(['Data', 'Descrição', 'Valor'])

    # Preencher o CSV com os dados
    for item in data:
        writer.writerow([item['date'], item['description'], item['amount']])

    return response
