# Generated by Django 2.2.4 on 2019-08-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('col', '0009_auto_20190811_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='is_active',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=10),
        ),
    ]