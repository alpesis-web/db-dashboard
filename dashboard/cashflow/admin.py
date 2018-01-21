from django.contrib import admin

from .models import ExpenseDict
from .models import IncomeDict
from .models import Expense
from .models import Income

admin.site.register(ExpenseDict)
admin.site.register(IncomeDict)
admin.site.register(Expense)
admin.site.register(Income)
