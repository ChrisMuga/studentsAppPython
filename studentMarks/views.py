from django.shortcuts import render
from django.http import HttpResponse
from .models import User

app_templates = {
    'student_registration': 'studentMarks/index.html'
}


def index(request):
    context = "Student Registration"
    return render(request, app_templates["student_registration"], {
        'context': context
    })


def new_user(request):
    # TODO: error handling
    # TODO: redirects
    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    current_class = request.POST.get("currentClass")
    email_address = request.POST.get("emailAddress")
    date_of_birth = request.POST.get("dateOfBirth")
    current_stream = request.POST.get("currentStream")

    register_user = User(
        firstName=first_name,
        lastName=last_name,
        currentClass=current_class,
        emailAddress=email_address,
        dateOfBirth=date_of_birth,
        currentStream=current_stream
    )

    register_user.save()

    return HttpResponse(register_user.id)
