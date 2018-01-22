from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('expensedict/', views.expensedict, name='expensedict'),
    path('expense/', views.expense, name='expense'),
    path('expense_monthly/', views.expense_monthly, name='expense_monthly'),
    path('incomedict/', views.incomedict, name='incomedict'),
    path('income/', views.income, name='income'),
    path('income_monthly/', views.income_monthly, name='income_monthly'),
]
