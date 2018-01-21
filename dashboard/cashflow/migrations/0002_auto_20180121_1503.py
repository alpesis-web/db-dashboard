# Generated by Django 2.0.1 on 2018-01-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expense',
            name='itemid',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expense',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
