from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    path('user/', include('api.user.urls')),
    path('groups/', include('api.groups.urls')),
    path('expense/', include('api.expense.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
