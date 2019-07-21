from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
from django.contrib import messages

app_templates = {
    'student_registration': 'studentMarks/student_registration.html',
    'students_list': 'studentMarks/students.html'
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

    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    current_class = request.POST.get("currentClass")
    email_address = request.POST.get("emailAddress")
    date_of_birth = request.POST.get("dateOfBirth")
    current_stream = request.POST.get("currentStream")

    try:
        user = User(
            firstName=first_name,
            lastName=last_name,
            currentClass=current_class,
            emailAddress=email_address,
            dateOfBirth=date_of_birth,
            currentStream=current_stream
        )

        user.save()

        response = {
            "code": 1,
            "msg": "User registration successful",
        }
        messages.success(request, response["msg"])
    except IntegrityError:
        response = {
            "code": 0,
            "msg": "Integrity Error"
        }
        messages.error(request, response.msg)
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

    student = User.objects.get(emailAddress=email_address)

    student.firstName = first_name
    student.lastName = last_name
    student.currentClass = current_class
    student.emailAddress = email_address
    student.dateOfBirth = date_of_birth
    student.currentStream = current_stream

    try:
        student.save()
        response = {
            "code": 1,
            "msg": "Update successful",
        }
        messages.success(request, response["msg"])
    except:
        response = {
            "code": 0,
            "msg": "Something went wrong. Update successful",
        }
        messages.error(request, response.msg)
    return redirect("students")



