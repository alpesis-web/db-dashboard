from django.contrib import admin

from .models import Expense
from .models import Income

admin.site.register(Expense)
admin.site.register(Income)
