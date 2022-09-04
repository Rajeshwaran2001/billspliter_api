import uuid

from django.db import models
from api.groups.models import group, Member
from api.user.models import CustomUser


# Create your models here.
class Debt(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_user')
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.to_user.name} owes {self.amount} to {self.from_user.name}'

class ExpenseUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    paid_share = models.IntegerField(default=0)
    owed_share = models.IntegerField(default=0)
    net_balance = models.IntegerField(default=0)


class Expense(models.Model):
    name = models.CharField(max_length=255, unique=False)
    expense_group = models.ForeignKey(group, on_delete=models.DO_NOTHING, null=True, db_constraint=False)
    description = models.CharField(max_length=255)
    payment = models.BooleanField(default=False)#
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    repayments = models.ManyToManyField(Debt)
    users = models.ManyToManyField(ExpenseUser)
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
