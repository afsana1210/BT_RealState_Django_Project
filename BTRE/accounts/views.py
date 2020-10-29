from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request,'that username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                  messages.error(request,'that email is being used')
                  return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)

                    user.save()
                    messages.success(request,'you are now register and can log in')
                    return redirect('login')
        else:
            messages.error(request,'password do not match')
            return redirect('register')
    else:
       return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        print('hello,this is post method')
        username=request.POST['username']
        password=request.POST['password']
        print('auth user')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            print('user not none')
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
      return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')
