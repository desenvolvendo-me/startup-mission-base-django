# Generated by Django 5.1 on 2024-08-16 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
