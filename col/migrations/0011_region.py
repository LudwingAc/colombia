# Generated by Django 2.2.4 on 2019-08-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('col', '0010_auto_20190811_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.IntegerField(unique=True)),
                ('municipios', models.ManyToManyField(to='col.municipioA')),
            ],
        ),
    ]
