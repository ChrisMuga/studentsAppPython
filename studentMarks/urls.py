from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-user', views.new_user),
    path('students-list', views.students, name="students"),
    path('update-student-details', views.update_student_details)
]