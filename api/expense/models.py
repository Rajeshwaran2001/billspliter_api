from django.db import models
from datetime import datetime
from api.groups.models import group,Member
# Create your models here.
class Expense(models.Model):
    title = models.CharField(null=True, max_length=100)
    price = models.FloatField(null=True)
    group = models.ForeignKey(group, null=True, on_delete=models.CASCADE)
    paid_date = models.DateTimeField(default=datetime.now(), null=True)
    paid_by = models.ForeignKey(Member, related_name='paid_by', on_delete=models.CASCADE, null=True)
    split_with = models.ManyToManyField(Member, related_name='expense_split')
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
