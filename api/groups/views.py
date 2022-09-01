from rest_framework import viewsets

from .models import group
from .serializers import GroupSerializer


# Create your views here.

class GroupViewSet(viewsets.ModelViewSet):
    queryset = group.objects.all()
    serializer_class = GroupSerializer
