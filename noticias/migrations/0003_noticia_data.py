# Generated by Django 2.0.13 on 2019-06-09 18:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_noticia_capa'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='data',
            field=models.DateField(default=datetime.datetime(2019, 6, 9, 18, 34, 4, 581837, tzinfo=utc)),
        ),
    ]
