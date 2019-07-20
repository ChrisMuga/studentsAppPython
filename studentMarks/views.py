from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError

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
    # TODO: CleanUp Session / Flush
    # TODO: NOT NULL = true on User model
    # TODO: Update Student Details

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

    except IntegrityError:
        response = {
            "code": 0,
            "msg": "Integrity Error"
        }

    # return HttpResponse(response)
    request.session["response"] = response
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
    except:
        response = {
            "code": 0,
            "msg": "Something went wrong. Update successful",
        }

    request.session["response"] = response
    return redirect("students")



