from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('expense/', views.expense, name='expense'),
    path('income/', views.income, name='income'),
    path('expensedict/', views.expensedict, name='expensedict'),
    path('incomedict/', views.incomedict, name='incomedict'),
]
