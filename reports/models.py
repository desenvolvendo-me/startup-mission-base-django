from django.db import models

# Modelo para armazenar os dados mensais
class MonthlyData(models.Model):
    month = models.IntegerField()  # Mês representado como um número de 1 a 12
    year = models.IntegerField()   # Ano
    data_value = models.FloatField()  # O valor do dado a ser analisado, pode ser adaptado

    class Meta:
        unique_together = ('month', 'year')
        verbose_name = 'Dado Mensal'
        verbose_name_plural = 'Dados Mensais'

    def __str__(self):
        return f"{self.month}/{self.year} - {self.data_value}"

# Modelo para armazenar os dados anuais
class YearlyData(models.Model):
    year = models.IntegerField(unique=True)  # Ano
    total_value = models.FloatField()  # Valor total dos dados do ano

    class Meta:
        verbose_name = 'Dado Anual'
        verbose_name_plural = 'Dados Anuais'

    def __str__(self):
        return f"{self.year} - {self.total_value}"

# Modelo para gerar os relatórios
class Report(models.Model):
    report_name = models.CharField(max_length=255)  # Nome do Relatório
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do relatório
    report_type = models.CharField(max_length=50, choices=[('CSV', 'CSV'), ('PDF', 'PDF')])  # Tipo de Relatório

    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'

    def __str__(self):
        return f"Relatório: {self.report_name} ({self.report_type}) - {self.created_at}"

    def generate_report(self):
        # Lógica para gerar o relatório,
        # calculando os dados necessários e exportando para CSV ou PDF.
        pass
