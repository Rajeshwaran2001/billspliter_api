from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('id', 'title', 'price', 'group', 'paid_date','paid_by','split_with','created_by','comment')
