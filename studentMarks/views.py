from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponse
from  django.contrib.auth.hashers import make_password

app_templates = {
    'student_registration': 'studentMarks/student_registration.html',
    'students_list': 'studentMarks/students.html',
    'login': 'studentMarks/login.html'
}


def index(request):
    context = "Student Registration"
    return render(request, app_templates["student_registration"], {
        'context': context,
    })


def new_user(request):
    # TODO: Use Django Messages Instead of Session.
    # TODO: NOT NULL = true on User model
    # TODO: Delete User
    username = request.POST.get("username")
    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    current_class = request.POST.get("currentClass")
    email_address = request.POST.get("emailAddress")
    date_of_birth = request.POST.get("dateOfBirth")
    current_stream = request.POST.get("currentStream")
    password = request.POST.get("password")

    password_hash = make_password(password, salt=None, hasher='default')

    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            currentClass=current_class,
            email=email_address,
            dateOfBirth=date_of_birth,
            currentStream=current_stream,
            username=username,
            password=password_hash
        )

        user.save()

        response = {
            "code": 1,
            "msg": "User registration successful",
        }
        messages.success(request, response["msg"])
    except IntegrityError as err:
        response = {
            "code": 0,
            "msg": "Integrity Error"
        }
        messages.error(request, response['msg'])
        print(err)
    return redirect("index")


def students(request):
    context = "Students"
    students = User.objects.all()
    return render(request, app_templates["students_list"], {
        'context': context,
        'students': students
    })


def update_student_details(request):
    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    current_class = request.POST.get("currentClass")
    email_address = request.POST.get("emailAddress")
    date_of_birth = request.POST.get("dateOfBirth")
    current_stream = request.POST.get("currentStream")

    try:
        student = User.objects.get(emailAddress=email_address)
        student.firstName = first_name
        student.lastName = last_name
        student.currentClass = current_class
        student.emailAddress = email_address
        student.dateOfBirth = date_of_birth
        student.currentStream = current_stream
        student.save()
        response = {
            "code": 1,
            "msg": "Update successful",
        }
        messages.success(request, response["msg"])
    except ObjectDoesNotExist:
        HttpResponse("Hello")
        response = {
            "code": 0,
            "msg": f"Error! Email - {email_address} does not exist",
        }
        messages.error(request, response["msg"])
    return redirect("students")


def login(request):
    context = "Login"
    return render(request, app_templates['login'], {
        "context": context
    })

def user_login(request):
    pass




