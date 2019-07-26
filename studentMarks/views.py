from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from studentMarks.templates.studentMarks.Template import Template

# import student marks template class
StudentMarksTemplate = Template()


def index(request):
    context = "Student Registration"
    return render(request, StudentMarksTemplate.student_registration, {
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


@login_required()
def students(request):
    context = "Students"
    students = User.objects.all()
    return render(request, StudentMarksTemplate.students_list, {
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
    if request.user.is_authenticated:
        return redirect("/dashboard")
    else:
        # check if there is a next field
        if "next" in request.GET and request.GET["next"] is not None:
            messages.info(request, "Welp! You have to log in to see that.")
        context = "Login"
        return render(request, StudentMarksTemplate.login, {
            "context": context
        })


def user_login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        auth_login(request, user)
        response = f"Welcome, {user.first_name}."
        messages.success(request, response)
        return redirect("/dashboard")
    else:
        response = "Invalid email-address or password"
        messages.error(request, response)
        return redirect("/")


@login_required()
def dashboard(request):
    context = "Dashboard"
    return render(request, StudentMarksTemplate.dashboard, {
        "context": context
    })


def logout(request):
    name = request.user.first_name
    messages.info(request, f"{name} just logged out")
    auth_logout(request)
    return redirect("/")



