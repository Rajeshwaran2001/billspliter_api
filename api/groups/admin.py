from django.contrib import admin

from api.groups.models import group,Member

# Register your models here.
admin.site.register(group)
admin.site.register(Member)
