# Generated by Django 2.0.13 on 2019-06-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0006_auto_20190612_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateTimeField(),
        ),
    ]