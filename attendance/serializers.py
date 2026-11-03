from rest_framework import serializers
from accounts.models import CustomUser
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role="STUDENT")
    )
    class Meta:
        model = Attendance
        fields = ['user', 'date', 'status']
        