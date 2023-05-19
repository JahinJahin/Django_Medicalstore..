import dataclasses
from imaplib import _Authenticator
from pickle import OBJ
from django.contrib.auth.forms import UserCreationForm,User
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from catalog.Forms import medicineForms, signform
from django.contrib.auth import authenticate,login,logout
from catalog.models import medicine

# Create your views here.



def base(request):
    return render(request,"base.html")


def loginform(request):
    if request.method == "POST":
        name=request.POST.get('username')
        password1=request.POST.get('password1')

        user= authenticate(username=name,password=password1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request,"login.html")


def register(request):
    if request.method =="POST":
        name  =request.POST['username']
        email =request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form=signform()

     
    return render(request,"register.html")

def home (request):
  
    obj = medicine.objects.all()
    return render(request,'home.html',{'data':obj})


def create(request):
    if request.method == 'POST':
        form =medicineForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request,'create.html')



def edit(request,id):
        obj =medicine.objects.get(id=id)
        form=medicineForms(instance=obj)
        if request.method == "POST":
          form = medicineForms(request.POST,instance=obj)
          if form.is_valid():
            form.save()
            return redirect("home")
          

        return render(request,'edit.html',{'form':obj})


def delete(request,id):
    obj = medicine.objects.get(id=id)
    obj.delete()
 
    return redirect ('home')

def logout(request):
    auth.logout(request)
    return redirect('login')
