from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['user', 'date', 'status']
        read_only_fields = ('user', 'date')
        