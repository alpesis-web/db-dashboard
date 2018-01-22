from django.shortcuts import render
from django.http import HttpResponse

from .models import Income
from .models import Expense

def index(request):
    return HttpResponse("Cashflow Platform")

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
