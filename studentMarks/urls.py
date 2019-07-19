from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-user', views.new_user)
]