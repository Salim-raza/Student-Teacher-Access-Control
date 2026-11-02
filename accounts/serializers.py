from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'role', 'password', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')
        
    def validate_role(self, value):
        value = value.upper()
        
        if value == "ADMIN":
            raise serializers.ValidationError(
                "You cannot register as admin."
            )
            
        allowed_roles = [CustomUser.Roles.STUDENT, CustomUser.Roles.TEACHER]
        
        if value not in allowed_roles:
            raise serializers.ValidationError(
                f"Invalid role. Must be one of {allowed_roles}."
            )
            
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            role=validated_data.get('role', CustomUser.Roles.STUDENT)
        )
