
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course


def home(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    context = {
        'students': students,
        'courses': courses,
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return HttpResponse("Contact Student Portal")
