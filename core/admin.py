
from django.contrib import admin
from .models import Student, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')
    search_fields = ('name', 'email')
    list_filter = ('age',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'duration')
    search_fields = ('course_name',)
    list_filter = ('duration',)
