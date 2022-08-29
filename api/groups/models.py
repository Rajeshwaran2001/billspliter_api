
from api.user.models import CustomUser
from django.db import models


# Create your models here.
class group(models.Model):
    Group_Name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    group_icon = models.ImageField(upload_to='./group_icons', max_length=100)
    Members = models.ManyToManyField(CustomUser, through='Member')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Group_Name


class Member(models.Model):
    user = models.ForeignKey(CustomUser, null=True, default=1, on_delete=models.CASCADE)
    group = models.ForeignKey(group, null=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, null=True, decimal_places=2, default=0)

    def __str__(self):
        return self.user.name
