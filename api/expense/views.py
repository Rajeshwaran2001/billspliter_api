from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.groups.models import group, Member
from api.expense import models, serializers
from .serializers import ExpenseSerializer


# Create your views here.

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = ExpenseSerializer


class CreateExpenseApiView(APIView):
    """Group Creation View"""
    serializer_class = serializers.ExpenseSerializer

    def post(self, request) -> Response:
        description = request.data.get('description')
        all_users = request.data.get('users')
        all_users = models.CustomUser.objects.filter(email__in=all_users)
        paid_by = request.data.get('paid_by')
        paid_by_user = models.CustomUser.objects.filter(email=paid_by).first()
        amount = request.data.get('amount')
        Group_Name = request.data.get('Group_Name', None)
        expense_name = request.data.get('name')

        if Group_Name is not None:
            group_name = models.group.objects.get(Group_Name=Group_Name)
        per_member_share = amount / len(all_users)
        expense_users = []
        repayments = []
        for user in all_users:
            if user != paid_by_user:
                debt = models.Debt.objects.create(**{"from_user": paid_by_user,
                                                     "to_user": user,
                                                     "amount": per_member_share})
                repayments.append(debt)
            expense_user_dict = {"user": user,
                                 "paid_share": 0 if user != paid_by_user else per_member_share,
                                 "owed_share": per_member_share,
                                 "net_balance": -per_member_share if user != paid_by_user else amount - per_member_share
                                 }
            expense_user = models.ExpenseUser.objects.create(**expense_user_dict)
            expense_users.append(expense_user)
        # now create expense
        expense = {
            'expense_group': group_name,
            'description': description,
            'amount': amount,
            'name': expense_name
        }
        expense = models.Expense.objects.create(**expense)
        expense.repayments.set(repayments)
        expense.users.set(expense_users)
        expense.save()
        return Response({'message': 'Expense Created successfully'})


class CreatePersonalExpenseApiView(APIView):
    """Group Creation View"""
    serializer_class = serializers.ExpenseSerializer

    def post(self, request) -> Response:
        description = request.data.get('description')
        all_users = request.data.get('users')
        all_users = models.CustomUser.objects.filter(email__in=all_users)
        paid_by = request.data.get('paid_by')
        paid_by_user = models.CustomUser.objects.filter(email=paid_by).first()
        amount = request.data.get('amount')
        group_name = request.data.get('Group_Name', None)
        expense_name = request.data.get('name')

        group = None
        if group_name is not None:
            group = models.group.objects.get(group_name=group_name)
        per_member_share = amount / len(all_users)
        expense_users = []
        repayments = []
        for user in all_users:
            if user != paid_by_user:
                debt = models.Debt.objects.create(**{"from_user": paid_by_user,
                                                     "to_user": user,
                                                     "amount": per_member_share})
                repayments.append(debt)
            expense_user_dict = {"user": user,
                                 "paid_share": 0 if user != paid_by_user else per_member_share,
                                 "owed_share": per_member_share,
                                 "net_balance": -per_member_share if user != paid_by_user else amount - per_member_share
                                 }
            expense_user = models.ExpenseUser.objects.create(**expense_user_dict)
            expense_users.append(expense_user)
        # now create expense
        expense = {
            'expense_group': group,
            'description': description,
            'amount': amount,
            'name': expense_name
        }
        expense = models.Expense.objects.create(**expense)
        expense.repayments.set(repayments)
        expense.users.set(expense_users)
        expense.save()
        return Response({'message': 'Expense Created successfully'})


class RecordPaymentApiView(APIView):
    def post(self, request) -> Response:
        from_user_email = request.data.get('from_user')
        to_user_email = request.data.get('to_user')
        amount = request.data.get('amount')
        Group_Name = request.data.get('Group_Name')
        expense_name = request.data.get('expense_name')
        from_user = models.CustomUser.objects.get(email=from_user_email)
        to_user = models.CustomUser.objects.get(email=to_user_email)
        try:
            if Group_Name is None:

                models.Debt.objects.create(**{
                    "from_user": from_user,
                    "to_user": to_user,
                    "amount": amount
                })
                return Response({
                    "message": "Payment Added successfully"
                })
            else:
                expense = models.Expense.objects.get(name=expense_name)
                if expense.expense_group != models.group.objects.get(group_name=Group_Name):
                    return Response({
                        "message": "Expense  not in group, please check !"
                    }, status=status.HTTP_400_BAD_REQUEST)
                flag = False
                for i in expense.repayments.all():
                    if i.from_user == to_user and i.to_user == from_user:
                        flag = True
                        i.amount = i.amount - amount
                        i.save()
                        break
                if not flag:
                    debt = models.Debt.objects.create(**{
                        "from_user": to_user,
                        "to_user": from_user,
                        "amount": amount
                    })
                    expense.repayments.add(debt)
                expense.save()
                flag = False
                for i in expense.repayments.all():
                    if i.amount > 0:
                        flag = True
                        break
                if not flag:
                    expense.payment = True
                    expense.save()
                return Response({
                    "message": "Expense Payment Added successfully"
                })
        except models.CustomUser.DoesNotExist:
            return Response({
                "message": "User does not exist"
            })
        except models.Expense.DoesNotExist:
            return Response({
                "message": "Expense does not exist"
            })


class RecordPersonalPaymentApiView(APIView):
    def post(self, request) -> Response:
        from_user_email = request.data.get('from_user')
        to_user_email = request.data.get('to_user')
        amount = request.data.get('amount')
        Group_Name = request.data.get('Group_Name')
        expense_name = request.data.get('expense_name')
        from_user = models.CustomUser.objects.get(email=from_user_email)
        to_user = models.CustomUser.objects.get(email=to_user_email)
        try:
            if Group_Name is None:

                models.Debt.objects.create(**{
                    "from_user": from_user,
                    "to_user": to_user,
                    "amount": amount
                })
                return Response({
                    "message": "Payment Added successfully"
                })
            else:
                expense = models.Expense.objects.get(name=expense_name)
                if expense.expense_group != models.group.objects.get(group_name=Group_Name):
                    return Response({
                        "message": "Expense  not in group, please check !"
                    }, status=status.HTTP_400_BAD_REQUEST)
                flag = False
                for i in expense.repayments.all():
                    if i.from_user == to_user and i.to_user == from_user:
                        flag = True
                        i.amount = i.amount - amount
                        i.save()
                        break
                if not flag:
                    debt = models.Debt.objects.create(**{
                        "from_user": to_user,
                        "to_user": from_user,
                        "amount": amount
                    })
                    expense.repayments.add(debt)
                expense.save()
                flag = False
                for i in expense.repayments.all():
                    if i.amount > 0:
                        flag = True
                        break
                if not flag:
                    expense.payment = True
                    expense.save()
                return Response({
                    "message": "Expense Payment Added successfully"
                })
        except models.CustomUser.DoesNotExist:
            return Response({
                "message": "User does not exist"
            })
        except models.Expense.DoesNotExist:
            return Response({
                "message": "Expense does not exist"
            })
