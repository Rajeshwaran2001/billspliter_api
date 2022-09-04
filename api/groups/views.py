from rest_framework import viewsets
from api.expense.models import Expense
from api.groups import models
from .serializers import GroupSerializer, MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ShowGroupsApiView(APIView):
    def get(self, request) -> Response:
        member = request.GET['name']
        try:
            member = models.Member.objects.filter(user=member)
            all_group = [x.group for x in member]
            return Response({'message': f'{all_group}'})
        except models.group.DoesNotExist:
            return Response(
                {'message': 'Group Does not exist !'
                 },
                status=status.HTTP_404_NOT_FOUND
            )


class ShowGroupMembersApiView(APIView):
    def get(self, request) -> Response:
        """ Create a hello message with our name """
        group_name = request.GET['name']
        try:
            group = models.group.objects.get(Group_Name=group_name)
            # all_members = [x.name for x in group.members]
            all_members = [str(x) for x in group.members.all()]
            return Response({'message': f'{all_members}'})
        except models.group.DoesNotExist:
            return Response(
                {'message': 'Group Does not exist !'
                 },
                status=status.HTTP_404_NOT_FOUND
            )


class AddUserToGroupApiView(APIView):
    """Add member to existing group Creation View"""

    def post(self, request) -> Response:
        """ Create a hello message with our name """
        Group_Name = request.data.get('Group_Name')
        user_email = request.data.get('email')
        user = models.CustomUser.objects.get(email=user_email)
        group = models.group.objects.get(Group_Name=Group_Name)
        if user not in group.members.all():
            group.members.add(user.id)
            return Response({'message': f'User successfully added to group {group.Group_Name}'})
        return Response({'message': 'User already exists in the group'}, status=status.HTTP_400_BAD_REQUEST)


class ShowGroupDetailsApiView(APIView):
    def get(self, request) -> Response:
        group_name = request.GET['name']
        try:
            group = models.group.objects.get(Group_Name=group_name)
            expenses = Expense.objects.filter(expense_group=group, payment=False)
            data = list()
            for expense in expenses:
                exp = {
                    "name": expense.name,
                    "Description": expense.description,
                    "repayments": [str(x) for x in expense.repayments.all() if
                                   x.from_user != x.to_user and x.amount != 0]
                }
                data.append(exp)
            return Response(
                {'message': data
                 }
            )
        except models.group.DoesNotExist:
            return Response(
                {'message': 'Group Does not exist !'
                 },
                status=status.HTTP_404_NOT_FOUND
            )

class DeleteGroupApiView(APIView):
    def delete(self, request) -> Response:
        group_name = request.GET['name']
        try:
            group = models.group.objects.get(Group_Name=group_name)
            if group:
                group.delete()
                return Response(
                    {
                        'message': 'Group deleted'
                    }
                )
        except models.group.DoesNotExist:
            return Response({
                "message": "Group does not exist"
            })

class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.group.objects.all()
    serializer_class = GroupSerializer
