from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('showMembersGroup', views.ShowGroupsApiView.as_view()),  ## to show group members
    path('showGroupMembers', views.ShowGroupMembersApiView.as_view()),  ## to show group members
    path('addUserToGroup', views.AddUserToGroupApiView.as_view()),  ## to add user to groups
]
