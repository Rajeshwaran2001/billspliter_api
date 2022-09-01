from rest_framework import serializers

from .models import group, Member


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    group_icon = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = group
        fields = ('id', 'Group_Name', 'description', 'group_icon', 'members')
