# Generated by Django 3.0.6 on 2020-05-27 17:35

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200527_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem do projeto'),
        ),
    ]