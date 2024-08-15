from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User


class Client(TenantMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='Client'
    )
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True


class Domain(DomainMixin):
    pass
