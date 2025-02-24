from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views.AuthViews import RegisterViewApi, LoginViewApi, CustomTokenObtainPairViewApi
from .views.DashboardViews import DashboardViewApi, AdminDashboardViewApi, TeacherDashboardViewApi

urlpatterns = [
    # API
    path('register/', RegisterViewApi.as_view(), name='register-api'),
    # path('login/', LoginViewApi.as_view(), name='login-api'),
    path('login/', CustomTokenObtainPairViewApi.as_view(), name='token-obtain-pair-api'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('dashboard/', DashboardViewApi.as_view(), name='dashboard-api'),
    path('dashboard/admin/', AdminDashboardViewApi.as_view(), name='dashboard-admin-api'),
    path('dashboard/teacher/', TeacherDashboardViewApi.as_view(), name='dashboard-teacher-api'),
]
