from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    appTemplates = {
        'student_registration': 'studentMarks/index.html'
    }
    context = "Student Registration"
    return render(request, appTemplates["student_registration"], {
        'context': context
    })


def new_user(request):
    return HttpResponse(request)
