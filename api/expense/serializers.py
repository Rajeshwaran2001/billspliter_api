from rest_framework import serializers

from .models import Expense, Debt, ExpenseUser


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('name', 'expense_group',
                  'description', 'payment',
                  'amount', 'repayments','users', 'transaction_id')


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'from_user', 'to_user', 'amount')


class ExpenseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseUser
        fields = ('id', 'paid_share', 'owed_share', 'net_balance')
