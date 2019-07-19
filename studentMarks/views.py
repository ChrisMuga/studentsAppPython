from django.shortcuts import render, redirect
from django.core import serializers
from .models import User
from django.db import IntegrityError

app_templates = {
    'student_registration': 'studentMarks/index.html'
}


def index(request):
    context = "Student Registration"
    return render(request, app_templates["student_registration"], {
        'context': context,
    })
    print(request.GET["data"])
    print(request.POST["data"])


def new_user(request):
    # TODO: CleanUp Session / Flush?
    # TODO: Start with partials.
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

    except IntegrityError as error:
        response = {
            "code": 0,
            "msg": "Integrity Error"
        }

    # return HttpResponse(response)
    request.session["response"] = response
    return redirect("index")



