# Generated by Django 5.0.6 on 2024-08-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTMaisapp', '0013_alter_pessoa_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
