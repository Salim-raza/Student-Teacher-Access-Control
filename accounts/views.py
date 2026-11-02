from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .utils import get_tokens_for_user
from rest_framework import status
from .models import CustomUser


# Create your views here.
class UserListView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response({"users": serializer.data}, status=status.HTTP_200_OK)



class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({"message": "Login successful.", "token": token}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user is not None:
            new_password = request.data.get('new_password')
            if new_password:
                user.set_password(new_password)
                user.save()
                return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)
            return Response({"message": "New password not provided."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)
            