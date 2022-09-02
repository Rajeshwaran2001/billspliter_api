from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import group
from .serializers import GroupSerializer


# Create your views here.
def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Please re-login', 'code': '1'})

    if request.method == "POST":
        user_id = id
        Group_Name = request.POST['Group_Name']
        description = request.POST['description']
        group_icon = request.POST['group_icon']
        members = request.POST['members']

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'})

        grp = group(user=user, Group_Name=Group_Name,description=description, group_icon=group_icon,members=members )

        grp.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Group Created Successfully'})


class GroupViewSet(viewsets.ModelViewSet):
    queryset = group.objects.all()
    serializer_class = GroupSerializer
