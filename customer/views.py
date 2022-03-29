from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def Main(request):
    return render(request,'drivers/index.html')

def Register(request):
    return render(request,'drivers/register.html')

def Login(request):
    return render(request,'drivers/login.html')

def RegisterUser(request):  
    try:
        print("--------------1---------------")
        fullname=request.POST['fname']
        username=request.POST['uname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        reapeatpassword=request.POST['reapeatpassword']
        user = User.objects.filter(email=email)
        if user:
            print("--------------2---------------")
            message = 'This email already exists'
            return render(request,("drivers/register.html"), {'message': message})
        else:
            if password == reapeatpassword:
                print("--------------3---------------")
                otp = randint(100000,9999999)
                newuser = User.objects.create(
                    email=email, password=password,otp=otp,username=username)
                newtech = customer.objects.create(user_id=newuser, fullname=fullname,phone=phone)
                return render(request,("drivers/login.html"))
            else:
                print("--------------4---------------")
                message = "Password and confirm password doesn't match"
                return render(request,("drivers/register.html"),{'message': message})
    
    except Exception as e1:
        print("Registration print---->",e1)

def LoginUser(request):
    # email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    if username == "admin@123" and password == "Admin@123":
        # return render(request,("drivers/adminhome.html"))
        return redirect('alldata')  
    else:
        user = User.objects.filter(username=username)
        print("---enter-----")
        if user[0].password == password:
            custo = customer.objects.filter(user_id=user[0])
            request.session['username']=user[0].username
            request.session['email']=user[0].email

            return render(request,("drivers/homepage.html"))
        else:

            message = "Your password is incorrect or user doesn't exist"
            return render(request, ("drivers/login.html"), {'message': message})


def AllData(request):
    alldata = User.objects.all()
    print(alldata)
    cont={'alldata':alldata}
    return render(request,("drivers/adminhome.html"),cont)

def Logout(request):
    logout(request)
    return render(request,("drivers/login.html"))   


def GetById(request):
    # getdata = customer.objects.get(pk=pk)
    return render(request,"login/editdetail.html")
    # {'key2':getdata}


