from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def register_user(request):
    return render(request,'register.html')
     


# register user
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
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
            message.error(request,"Passwords do not match")
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

        


                

                
        
    
    
    
    