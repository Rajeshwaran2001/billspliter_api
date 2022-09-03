from rest_framework import viewsets
from api.expense import models
from .serializers import ExpenseSerializer

# Create your views here.

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = ExpenseSerializer
