from django.contrib import admin
from .models import Expense,Debt,ExpenseUser
# Register your models here.
admin.site.register(Expense)
admin.site.register(Debt)
admin.site.register(ExpenseUser)


