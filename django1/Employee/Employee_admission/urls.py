from django.urls import path
from . import views

urlpatterns=[
    path("",views.welcome),
    path("profile/",views.profile),
    path("form/",views.form)
]