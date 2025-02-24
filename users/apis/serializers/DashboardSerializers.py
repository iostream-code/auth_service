from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class DashboardSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_users = serializers.IntegerField()
    new_users_today = serializers.IntegerField()
    users = serializers.ListField(
        child=serializers.DictField()
    )
