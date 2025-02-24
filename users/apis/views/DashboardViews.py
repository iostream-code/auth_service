from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from users.apis.permissions import IsAdmin, IsTeacher
from users.apis.serializers.DashboardSerializers import DashboardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()

class DashboardViewApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        new_users_today = User.objects.filter(date_joined__gte=now() - timedelta(days=1)).count()

        users = User.objects.values("username", "email", "is_active")

        data = {
            "total_users": total_users,
            "active_users": active_users,
            "new_users_today": new_users_today,
            "users": list(users),
        }

        serializer = DashboardSerializer(data)
        return Response(serializer.data)

class AdminDashboardViewApi(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome, Admin!"})

class TeacherDashboardViewApi(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        return Response({"message": "Welcome, Teacher!"})