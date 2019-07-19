from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def index(request):
    context = "Student Registration"
    return render(request, 'studentMarks/index.html', {
        'context': context
    })
