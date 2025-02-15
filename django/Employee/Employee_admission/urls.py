from django.urls import path
from . import views

urlpatterns=[
    path("",views.welcome),
    path("home/",views.home),
    path("gallery/",views.gallery),
    path("login/",views.login),
    path("profile/",views.profile),
    path("signup/",views.signup),
    path("add-department/",views.add),
    path("show-department/",views.get_department),
    path("delete-department/<int:id>",views.delete_department),
    path("update-department/<int:id>",views.update_department),
]