from django.urls import path, include
from .views import RegisterPageView, LoginPageView, DashboardPageView

urlpatterns = [
    # Template
    path('register/', RegisterPageView.as_view(), name='register-page'),
    path('login/', LoginPageView.as_view(), name='login-page'),
    
    # Dashboard
    path('dashboard/', DashboardPageView.as_view(), name='dashboard-page'),
    
    # Path APIS
    path('api/', include('users.apis.urls')),  
]
