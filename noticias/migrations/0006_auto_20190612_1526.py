# Generated by Django 2.0.13 on 2019-06-12 18:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_auto_20190612_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateField(default=datetime.datetime(2019, 6, 12, 18, 26, 50, 51861, tzinfo=utc)),
        ),
    ]
