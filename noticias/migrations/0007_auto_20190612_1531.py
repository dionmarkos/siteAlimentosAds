# Generated by Django 2.0.13 on 2019-06-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_auto_20190612_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateField(),
        ),
    ]
