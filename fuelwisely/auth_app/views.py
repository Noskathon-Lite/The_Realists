from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.

def Test(request):
    return HttpResponse("hello")
     


# register user
def register_user(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # confirm_password = request.POST['confirm_password']
        
        if password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already exists")
            elif User.object.filter(email=email).exists():
                messages.error(request,"email already exists")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,"User registered successfully! ")
                return redirect('login')
        else:
            messages.error(request,"Passwords do not match")
    return render(request,'register.html')

#login user 
def login_user(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request,'login.html')

#logout a user:
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('login')

        


                

                
        
    
    
    
    