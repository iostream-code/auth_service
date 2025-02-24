from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()

class LoginPageView(TemplateView):
    template_name = "auth/login.html"

class RegisterPageView(TemplateView):
    template_name = "auth/register.html"

class DashboardPageView(TemplateView):
    template_name = "dashboard.html"
