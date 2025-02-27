from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse

from employee.models import Department_details
from employee.models import Designation
from employee.models import Employee_details

# Create your views here.

# department
# user can view the webpage
def deptform(request):
    return render(request,'deptform.html')

# inserting  the data into the html form
def deptinsert(request):
    dept_name=request.POST.get('dept_name')
    dept_description=request.POST.get('dept_description')
    department=Department_details.objects.create(dept_name=dept_name,dept_description=dept_description)
    return redirect('deptlist')

# list the user data
def deptlist(request):
    departments = Department_details.objects.all()
    return render(request, 'deptlist.html', {'departments': departments})

#delete the data by using user_id 
def dept_delete(request,id):
    departments=Department_details.objects.get(id=id)
    departments.delete()
    return redirect('deptlist')

# get the html form for update with data
def dept_update(request,id):
    departments=Department_details.objects.get(id=id)
    return render(request,'deptupdate.html',{'departments':departments})

# insert the user data in updata form
def dept_details(request,id):
    departments=Department_details.objects.get(id=id)
    if request.method =='POST':
        departments.dept_name=request.POST.get('dept_name')
        departments.dept_description=request.POST.get('dept_description')
        departments.save()
    return redirect('deptlist')



# designation
# get the html form for user
def designationform(request):
    department=Department_details.objects.all()
    return render(request,'desform.html',{'dept':department})

#insert the data to html form  
def designationinsert(request):
    designation_name=request.POST.get('designation_name')
    designation_dept_id=request.POST.get('designation_dept')
    designation_description=request.POST.get('designation_description')
    designation_dept = Department_details.objects.get(id=designation_dept_id) 
    designation=Designation.objects.create(designation_name=designation_name,designation_dept=designation_dept,designation_description=designation_description)
    return redirect('deslist')

# list the user data 
def deslist(request):
    designations = Designation.objects.all()
    return render(request, 'deslist.html', {'designations': designations})

# delete the data using user_id
def des_delete(request,id):
    designations=Designation.objects.get(id=id)
    designations.delete()
    return redirect('deslist')

# get the update form by using user_id
def des_update(request,id):
    designations=Designation.objects.get(id=id)
    department=Department_details.objects.all()
    return render(request,'desupdate.html',{'designation':designations,'departments':department})

# insert data into updated html form
def des_details(request, id):
    
    designation = Designation.objects.get(id=id)
    designation.designation_name = request.POST.get('designation_name')
    designation_dept_id = request.POST.get('designation_dept')
    designation.designation_dept = Department_details.objects.get(id=designation_dept_id)
    designation.designation_description = request.POST.get('designation_description')
    
    designation.save()
    return redirect('deslist')  


# employee
# get html form from user 
def empform(request):
    department=Department_details.objects.all()
    designation=Designation.objects.all()
    return render(request,'empform.html',{'dept':department,'designations':designation})

# insert the data into the html form
def emp_insert(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    dob = request.POST.get('dob')
    address = request.POST.get('address')
    email = request.POST.get('email')
    emp_department_id = request.POST.get('department')
    emp_designation_id = request.POST.get('designation')
    doj = request.POST.get('doj')
    image = request.FILES.get('image')
    department = Department_details.objects.get(id=emp_department_id)
    designation = Designation.objects.get(id=emp_designation_id)
    emp = Employee_details.objects.create(
        name=name,
        gender=gender,
        dob=dob,
        address=address,
        email=email,
        department=department,
        designation=designation,
        doj=doj,
        image=image
    )
    return redirect('emplist')

# list the user from the form 
def emplist(request):
    emp=Employee_details.objects.all()
    return render(request,'emplist.html',{'emp':emp})

# delete the user_data by using user_id
def emp_delete(request,id):
    emp=Employee_details.objects.get(id=id)
    emp.delete()
    return redirect('emplist')

# get the update form from user by using user_id
def emp_update(request,id):
    emp=Employee_details.objects.get(id=id)
    department=Department_details.objects.all()
    designation=Designation.objects.all()
    return render(request,'empupdate.html',{'emp':emp,'departments':department,'designations':designation})

# insert the data into update form
def emp_details(request,id):
    emp=Employee_details.objects.get(id=id)
    
    if request.method =='POST':
        emp.name=request.POST.get('name')
        emp.gender=request.POST.get('gender')
        emp.dob=request.POST.get('dob')
        emp.address=request.POST.get('address')
        emp.email=request.POST.get('email')
        emp.doj=request.POST.get('doj')
        emp.image=request.FILES.get('image')
        department_id=request.POST.get('department')
        designation_id=request.POST.get('designation')
        emp.department=Department_details.objects.get(id=department_id)
        emp.designation=Designation.objects.get(id=designation_id)
        emp.save()
    return redirect('emplist')