from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Meta(models.Model):
    STATUS_CHOICES = [
        ('executando', 'Executando'),
        ('desistiu', 'Desistiu'),
        ('concluido', 'Concluído'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField()
    previsao_conclusao = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='executando')
    user=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='user_meta'
    )
    
    def __str__(self):
        return f"{self.nome} {self.descricao}"


class Task(models.Model):
    id=models.AutoField(
        primary_key=True
    )

    name=models.CharField(max_length=200)

    meta=models.ForeignKey(
        Meta, 
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='meta'
    )

    description=models.TextField(
        blank=False,
        null=False
    )

    is_active=models.BooleanField(
        default=True
    )

    user=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='user_task'
    )

    def __str__(self):
        return str(self.name)    

