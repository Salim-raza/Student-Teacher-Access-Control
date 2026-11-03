from django.urls import path
from .views import *



urlpatterns = [ 
    path('attendance-view/', AttendanceView.as_view(), name='attendance'),
    path('add-attendance/', MarkAttendanceView.as_view(), name='add-attendance'),
    path('student-attendance/', StudentAttendanceView.as_view(), name='student-attendance'),
    path('update-attendance/<int:pk>/', AttendanceUpdateView.as_view(), name='update-attendance'),
    path('delete-attendance/<int:pk>/', AttendanceDeleteView.as_view(), name='delete-attendance'),     
]