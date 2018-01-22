from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

from .models import Income
from .models import Expense
from .models import IncomeDict
from .models import ExpenseDict


# ----------------------------------------------------------------------------

def index(request):
    return render(request, "index.html")

# ----------------------------------------------------------------------------

def expense(request):
    expense_list = Expense.objects.order_by('year', 'month', 'date')[:]
    context = {
        'table_name': "Expense",
        'item_list': expense_list
    }
    return render(request, "entry.html", context)

def expensedict(request):
    expense_dict = ExpenseDict.objects.order_by('itemid')[:]
    context = {
        'table_name': "Expense Dictionary",
        'item_list': expense_dict
    }
    return render(request, "dict.html", context)

def expense_monthly(request):
    expense_monthly = Expense.objects.values('year', 'month').annotate(Sum('amount'))
    context = {
        "table_name": "Expense Monthly",
        "item_monthly": expense_monthly
    }
    return render(request, "report_monthly.html", context)


def expense_yearly(request):
    expense_yearly = Expense.objects.values('year').annotate(Sum('amount'))
    context = {
        "table_name": "Expense Yearly",
        "item_yearly": expense_yearly
    }
    return render(request, "report_yearly.html", context)

# ----------------------------------------------------------------------------

def income(request):
    income_list = Income.objects.order_by('year', 'month', 'date')[:]
    context = {
        'table_name': "Income",
        'item_list': income_list
    }
    return render(request, "entry.html", context)


def incomedict(request):
    income_dict = IncomeDict.objects.order_by('itemid')[:]
    context = {
        'table_name': "Income Dictionary",
        'item_list': income_dict
    }
    return render(request, "dict.html", context)


def income_monthly(request):
    income_monthly = Income.objects.values('year', 'month').annotate(Sum('amount'))
    context = {
        "table_name": "Income Monthly",
        "item_monthly": income_monthly
    }
    return render(request, "report_monthly.html", context)


def income_yearly(request):
    income_yearly = Income.objects.values('year').annotate(Sum('amount'))
    context = {
        "table_name": "Income Yearly",
        "item_yearly": income_yearly
    }
    return render(request, "report_yearly.html", context)
