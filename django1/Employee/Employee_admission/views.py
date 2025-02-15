from django.shortcuts import render,HttpResponse,get_object_or_404,redirect

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def profile(request):
    return render(request,"profile.html")

def form(request):
    return render(request,"Department/form.html")

