from django.shortcuts import render,redirect
from .models import*

# Create your views here.


def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')


def register1(request):
    obj=UInfo()
    obj.name=request.POST.get("name")
    obj.address=request.POST.get("address")
    obj.save()
    return redirect('register1')

    # return render(request,'success.html',{'name':name,'address':address})
