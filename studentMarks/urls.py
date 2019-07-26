from django.urls import path
from .views import User

urlpatterns = [
    path('register', User.index, name='index'),
    path('new-user', User.new_user),
    path('students-list', User.students, name="students"),
    path('update-student-details', User.update_student_details),
    path('', User.login),
    path('user-login', User.user_login),
    path('dashboard', User.dashboard),
    path("logout", User.logout)
]