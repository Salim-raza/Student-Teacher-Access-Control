from django.contrib import admin
from .models import Attendance

# Register your models here.
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('user__email', 'date')
