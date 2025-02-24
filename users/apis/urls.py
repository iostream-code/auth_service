from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views.AuthViews import RegisterViewApi, LoginViewApi
from .views.DashboardViews import DashboardViewApi

urlpatterns = [
    # API
    path('register/', RegisterViewApi.as_view(), name='register-api'),
    path('login/', LoginViewApi.as_view(), name='login-api'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('dashboard/', DashboardViewApi.as_view(), name='dashboard-api'),
]
