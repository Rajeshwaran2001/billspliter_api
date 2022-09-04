from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('name', 'expense_group', 'description', 'payment', 'amount','date','repayments','users','transaction_id')
