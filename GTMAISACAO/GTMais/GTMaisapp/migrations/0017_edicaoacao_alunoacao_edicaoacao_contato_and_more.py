# Generated by Django 5.0.6 on 2024-08-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTMaisapp', '0016_acaoextensao_idcidade_acaoextensao_idestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicaoacao',
            name='alunoAcao',
            field=models.CharField(default='Leon Tassinari', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edicaoacao',
            name='contato',
            field=models.CharField(default='Leon@gmail.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edicaoacao',
            name='coordenadorAcao',
            field=models.CharField(default='Marco Silva', max_length=255),
            preserve_default=False,
        ),
    ]