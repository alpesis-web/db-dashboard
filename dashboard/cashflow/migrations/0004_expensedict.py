# Generated by Django 2.0.1 on 2018-01-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0003_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.BigIntegerField(default=0)),
                ('item', models.CharField(max_length=200)),
            ],
        ),
    ]
