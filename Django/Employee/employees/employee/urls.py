
from django.urls import path
from . import views

urlpatterns=[
    # department
    path('deptform',views.deptform,name='deptform'),
    path('deptinsert',views.deptinsert,name='deptinsert'),
    path('deptlist/',views.deptlist,name='deptlist'),
    path('department/<int:id>/delete/',views.dept_delete,name='deptdelete'),
    path('department/<int:id>/update_form/',views.dept_update,name='deptupdate'),
    path('department/<int:id>/update/',views.dept_details,name='deptdetails'),
    
    # designation
    path('desform',views.designationform,name='designationform'),
    path('desinsert',views.designationinsert,name='designationinsert'),
    path('deslist',views.deslist,name='deslist'),
    path('des/<int:id>/delete/',views.des_delete,name='desdelete'),
    path('des/<int:id>/update_form/',views.des_update,name='desupdate'),
    path('des/<int:id>/update/',views.des_details,name='desdetails'),
    
    # # /employees
    path('empform/',views.empform,name='empform'),
    path('empinsert',views.emp_insert,name='emp_insert'),
    path('emplist',views.emplist,name='emplist'),
    path('emp/<int:id>/delete/',views.emp_delete,name='emp_delete'),
    path('emp/<int:id>/update_form/',views.emp_update,name='emp_update'),
    path('emp/<int:id>/update/',views.emp_details,name='emp_details'),
]