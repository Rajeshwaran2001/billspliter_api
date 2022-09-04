from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addExpense', views.CreatePersonalExpenseApiView.as_view()),
    path('createExpense', views.CreateExpenseApiView.as_view()),
    path('recordPayment', views.RecordPaymentApiView.as_view()),
    path('recordPersonlPayment', views.RecordPersonalPaymentApiView.as_view()),

]
