from django.urls import path

from . import views

urlpatterns = [
    path('register', views.index, name='index'),
    path('new-user', views.new_user),
    path('students-list', views.students, name="students"),
    path('update-student-details', views.update_student_details),
    path('', views.login),
    path('user-login', views.user_login)
]