from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permission import IsTeacher, IsStudent
from .serializers import AttendanceSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Attendance

# Create your views here.

class AttendanceView(APIView):
    permission_classes = [IsTeacher]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        attendance_records = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance_records, many=True)
        return Response({"attendance": serializer.data}, status=status.HTTP_200_OK)
    
    
    
class MarkAttendanceView(APIView):
    permission_classes = [IsTeacher]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Attendance marked successfully."}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class StudentAttendanceView(APIView):
    permission_classes = [IsStudent]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        attendance_records = Attendance.objects.filter(user=request.user)
        serializer = AttendanceSerializer(attendance_records, many=True)
        return Response({"attendance": serializer.data}, status=status.HTTP_200_OK)
    
    
    
class AttendanceUpdateView(APIView):
    permission_classes = [IsTeacher]
    authentication_classes = [JWTAuthentication]
    
    def patch(self, request, pk):
        attendance = get_object_or_404(Attendance, pk=pk)
        serializer = AttendanceSerializer(attendance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Attendance updated successfully."}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class AttendanceDeleteView(APIView):
    permission_classes = [IsTeacher]
    authentication_classes = [JWTAuthentication]
    
    def delete(self, request, pk):
        attendance = get_object_or_404(Attendance, pk=pk)
        attendance.delete()
        return Response({"message": "Attendance deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

