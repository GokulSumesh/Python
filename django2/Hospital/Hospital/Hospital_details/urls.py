from django.urls import path
from . import views

urlpatterns=[
    path("",views.form),
    path("add-details/",views.add),
    path("show-details/",views.get_details),
    path("delete-details/<int:id>",views.delete_details),
    path("update-details/<int:id>",views.update_details),

]

