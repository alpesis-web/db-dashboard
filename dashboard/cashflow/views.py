from django.shortcuts import render
from django.http import HttpResponse

from .models import Income
from .models import Expense
from .models import IncomeDict
from .models import ExpenseDict


def index(request):
    return render(request, "index.html")

def expense(request):
    expense_list = Expense.objects.order_by('year', 'month', 'date')[:]
    context = {
        'table_name': "Expense",
        'item_list': expense_list
    }
    return render(request, "entry.html", context)

def income(request):
    income_list = Income.objects.order_by('year', 'month', 'date')[:]
    context = {
        'table_name': "Income",
        'item_list': income_list
    }
    return render(request, "entry.html", context)


def expensedict(request):
    expense_dict = ExpenseDict.objects.order_by('-item')[:]
    context = {
        'table_name': "Expense Dictionary",
        'item_list': expense_dict
    }
    return render(request, "dict.html", context)

def incomedict(request):
    income_dict = IncomeDict.objects.order_by('-item')[:]
    context = {
        'table_name': "Income Dictionary",
        'item_list': income_dict
    }
    return render(request, "dict.html", context)
