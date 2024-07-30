# Generated by Django 5.0.6 on 2024-07-30 17:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTMaisapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acaoextensao',
            name='dtCriacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acaoextensao',
            name='dtFim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acaoextensao',
            name='dtInicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acaoextensao',
            name='dtModificacao',
            field=models.DateField(blank=True, null=True),
        ),
    ]