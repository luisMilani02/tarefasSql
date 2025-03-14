# Generated by Django 5.1.6 on 2025-03-08 18:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefas',
            name='completa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarefas',
            name='criada',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='conteudoTarefa',
            field=models.CharField(max_length=200),
        ),
    ]
