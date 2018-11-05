# Generated by Django 2.1.2 on 2018-11-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181031_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='solicitado em'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='participation_on',
            field=models.DateField(auto_now_add=True, verbose_name='período da pesquisa'),
        ),
    ]