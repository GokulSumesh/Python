from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Details

# Create your views here.

def form(request):
    return render(request,"Details/form.html")

def add(request):
    Details.objects.create(name=request.POST["name"],phone = request.POST["phone"],email = request.POST["email"],street = request.POST["street"],city = request.POST["city"],district = request.POST["district"])
    return redirect("/hospital/show-details/")

def get_details(request):
    details = Details.objects.all()
    return render(request,"Details/table.html",{"details":details})

    
def delete_details(request,id):
    details = get_object_or_404(Details,id=id)
    details.delete()
    return redirect("/hospital/show-details/")

def update_details(request,id):
    details = get_object_or_404(Details,id=id)
    if request.method == "POST":
        details.name = request.POST["name"]
        details.phone = request.POST["phone"]
        details.email = request.POST["email"]
        details.street = request.POST["street"]
        details.city = request.POST["city"]
        details.district = request.POST["district"]
        details.save()
        return redirect("/hospital/show-details/")
    
    return render(request,"Details/edit.html",{"users":details})





 


 
