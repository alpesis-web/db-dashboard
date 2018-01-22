from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('expensedict/', views.expensedict, name='expensedict'),
    path('expense/', views.expense, name='expense'),
    path('expense_monthly/', views.expense_monthly, name='expense_monthly'),
    path('expense_yearly/', views.expense_yearly, name='expense_yearly'),
    path('incomedict/', views.incomedict, name='incomedict'),
    path('income/', views.income, name='income'),
    path('income_monthly/', views.income_monthly, name='income_monthly'),
    path('income_yearly/', views.income_yearly, name='income_yearly'),
]
