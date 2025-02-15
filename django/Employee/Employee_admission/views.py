from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Department

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def home(request):
    return render(request,"home.html")

def gallery(request):
    return render(request,"gallery.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")

def signup(request):
    return render(request,"Department/form.html")

def add(request):
    Department.objects.create(name=request.POST["name"],description = request.POST["description"])
    return redirect("/employee/show-department/")

def get_department(request):
    departments = Department.objects.all()
    return render(request,"Department/table.html",{"departments":departments})
    
def delete_department(request,id):
    department = get_object_or_404(Department,id=id)
    department.delete()
    return redirect("/employee/show-department/")


def update_department(request,id):
    department = get_object_or_404(Department,id=id)
    if request.method == "POST":
        department.name = request.POST["name"]
        department.description = request.POST["description"]
        department.save()
        return redirect("/employee/show-department/")
    
    return render(request,"Department/edit.html",{"users":department})
