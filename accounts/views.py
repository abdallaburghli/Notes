from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages , auth
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'loged in successfuly')
            return redirect('notes')
        else:
            messages.error(request,'Invalid Credetnials')
            return redirect('login')
    
                
    return render(request,'accounts/login.html')
    

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is used')
                return redirect('R egister')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                        username=username,email=email,password=password)
                    messages.success(request,'You are now registered')
                    user.save()
                    
                    return redirect('login')
        else:
            messages.error(request,'Passwords dont match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
    

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,'You Are Logged Out')

    return redirect('index')