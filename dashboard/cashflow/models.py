from django.db import models

class Expense(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    date = models.IntegerField(default=0)
    itemid = models.BigIntegerField(default=0)
    price = models.FloatField(default=0)


class Income(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    date = models.IntegerField(default=0)
    itemid = models.BigIntegerField(default=0)
    amount = models.FloatField(default=0)
