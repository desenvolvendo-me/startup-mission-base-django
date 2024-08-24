from django.db import models
from django.contrib.auth.models import User, AbstractUser

STATUS_CHOICES = [
    ('executando', 'Executando'),
    ('desistiu', 'Desistiu'),
    ('concluido', 'Concluído'),
]


class Meta(models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True) # O null e o teste é apenas para teste.
    previsao_conclusao = models.DateField(
        null=True,
        blank=True
    )
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
        null=True,
        blank=True,
        related_name='meta'
    )

    description=models.TextField(
        blank=False,
        null=False
    )
    created_at: models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(
        default=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='executando'
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

