# Generated by Django 5.0.6 on 2024-08-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTMaisapp', '0010_remove_acaoextensao_imagem_remove_contatoacao_imagem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='acaoextensao',
            name='imagem',
            field=models.ImageField(default='', upload_to='projectsimages/'),
            preserve_default=False,
        ),
    ]