ujkmh
abxk
Invisible

Phantom — Today at 8:26 AM
Image
Luffy — Today at 10:15 AM
from django.db import models

Step 2: Transportation Log
class TransportationLog(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(help_text="Reference to user ID from the auth app")
    date = models.DateField()
    vehicle_type = models.CharField(max_length=50, choices=[
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('bus', 'Bus'),
        ('train', 'Train'),
    ])
    distance = models.FloatField(help_text="Distance traveled in kilometers")
    mode = models.CharField(max_length=50, choices=[
        ('public', 'Public Vehicle'),
        ('private', 'Private Vehicle'),
    ])
    emissions = models.FloatField(help_text="CO2 emissions in grams")

    def str(self):
        return f"User ID {self.user_id} - {self.vehicle_type} on {self.date}"

Emission Summary
class EmissionSummary(models.Model):
    user_id = models.IntegerField(unique=True, help_text="Reference to user ID from the auth app")
    total_distance = models.FloatField(default=0.0, help_text="Total distance traveled in kilometers")
    total_emissions = models.FloatField(default=0.0, help_text="Total CO2 emissions in grams")

    def str(self):
        return f"Summary for User ID {self.user_id}"
Luffy — Today at 10:31 AM
from django.db import models

Create your models here.
class  Transportationmodel(models.Model):
    vehicle_type = models.CharField(max_length=50,choices=
                                       [
                                        ('car','Car'),
                                        ('bike','Bike')
                                        ('bus','Bus'),
                                        ('scooter','Scooter'),
                                       ]
                                    )
    distance = models.FloatField(distance_travelled = "Distance travelled in kilomeeters" )

    mode = models.CharField(max_length=50, choices=
                            [
                                ('public','Public'),
                                ('private','Private'),
                            ]
                            )
    emissions = models.FloatField(co2_emitted = "Co2 emmissions in grams ")

    def str(self):
        return 



class EmissionsSummary(models.Model):
    total_distance  = models.FloatField(default=0.0, traveled_distance = "total distance traveled in kilomeeters")
    total_emissions = models.FloatField(default=0.0,emission = "total co2 emissions ")
@ujkmh
Luffy — Today at 10:47 AM
from django.db import models

Create your models here.
class TransportationModel(models.Model):
    vehicle_type = models.CharField(max_length=50, choices=[
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('bus', 'Bus'),
        ('scooter', 'Scooter'),
    ])
    vehicle_size = models.CharField(max_length=50, choices=[
        ('small', 'Small'),
        ('average', 'Average'),
        ('large', 'Large'),
        ('big', 'Big'),
    ], help_text="Size category of the vehicle")
    distance = models.FloatField(help_text="Distance travelled in kilometers")
    mode = models.CharField(max_length=50, choices=[
        ('public', 'Public'),
        ('private', 'Private'),
    ])
    emissions = models.FloatField(help_text="CO2 emissions in grams")

    def str(self):
        return f"{self.vehicle_type} ({self.vehicle_size}) - {self.mode}"

class EmissionsSummary(models.Model):
    total_distance = models.FloatField(default=0.0, help_text="Total distance traveled in kilometers")
    total_emissions = models.FloatField(default=0.0, help_text="Total CO2 emissions in grams")

    def str(self):
        return f"Distance: {self.total_distance} km, Emissions: {self.total_emissions} g"
Luffy — Today at 11:15 AM
from django.db import models sum
Luffy — Today at 12:20 PM
abhiske
from django.db import models
from django.db.models import Sum
# Create your models here.
class  Transportationmodel(models.Model):
    vehicle_type = models.CharField(max_length=50,choices=
                                       [
Expand
message.txt
3 KB
Phantom — Today at 12:21 PM
from django.db import models
from django.contrib.auth.models import User
Create your models here.
class UserProfile(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def str(self):
        return self.name
Luffy — Today at 12:41 PM
from django.db import models
from django.db.models import Sum
# Create your models here.
class  Transportationmodel(models.Model):
    vehicle_type = models.CharField(max_length=50,choices=
                                       [
                                        ('car','Car'),
                                        ('bike','Bike'),
                                        ('bus','Bus'),
                                        ('scooter','Scooter'),
                                       ]
                                    )
    distance = models.FloatField(help_text = "Distance travelled in kilomeeters" )

    mode = models.CharField(max_length=50, choices=
                            [
                                ('public','Public'),
                                ('private','Private'),
                            ]
                            )
    vehicle_size = models.CharField(max_length=50, choices=[
        ('small', 'Small'),
        ('average', 'Average'),
        ('large', 'Large'),
        ('big', 'Big'),
    ], help_text ="Size category of the vehicle")
    emissions = models.FloatField(help_text = "Co2 emmissions in grams ")

    def __str__(self):
       return f"Transportation_Log:{self.vehicle_type} ({self.vehicle_size}) - {self.mode}"



class EmissionsSummary(models.Model):
    total_distance  = models.FloatField(default=0.0, help_text = "total distance traveled in kilomeeters")
    total_emissions = models.FloatField(default=0.0,help_text = "total co2 emissions ")

    def __str__(self):
        return f"Distance :{self.total_distance} km , Emissions : {self.total_emissions}" 

    @classmethod
    def calculate_totals(cls):
        
        total_distance  =  Transportationmodel.objects.aggregate(Sum('distance'))['distance__sum'] or 0.0
        total_emissions = Transportationmodel.objects.aggregate(Sum('emissions'))['emissions__sum'] or 0.0

                
        summary, created = cls.objects.get_or_create(id=1)
        summary.total_distance = total_distance
        summary.total_emissions = total_emissions
        summary.save()

        return summary
Collapse
message.txt
3 KB
ujkmh — Today at 1:33 PM
EMISSION_FACTORS = {
    'car': {'small': 135, 'average': 165, 'large': 215, 'big': 300},
    'bike': {'small': 45, 'average': 60, 'large': 85},
    'scooter': {'small': 35, 'average': 45, 'large': 60},
    'bus': {'small': 30, 'average': 40, 'large': 55},
    'train': {'electric': 20, 'diesel': 55},
}


@Luffy
def calculate_emissions(vehicle_type, vehicle_size, distance):
    # Get the emission factor for the vehicle type and size
    factor = EMISSION_FACTORS.get(vehicle_type, {}).get(vehicle_size, 0)
    # Calculate emissions
    return factor * distance


@Luffy
ujkmh — Today at 1:42 PM
from django.db import models
from django.db.models import Sum

# Emission Factors (CO₂ in grams per kilometer)
EMISSION_FACTORS = {
    'car': {'small': 135, 'average': 165, 'large': 215, 'big': 300},
    'bike': {'small': 45, 'average': 60, 'large': 85},
    'scooter': {'small': 35, 'average': 45, 'large': 60},
    'bus': {'small': 30, 'average': 40, 'large': 55},
    'train': {'electric': 20, 'diesel': 55},
}

# Transportation Model
class Transportationmodel(models.Model):
    vehicle_type = models.CharField(
        max_length=50,
        choices=[
            ('car', 'Car'),
            ('bike', 'Bike'),
            ('bus', 'Bus'),
            ('scooter', 'Scooter'),
        ]
    )
    distance = models.FloatField(help_text="Distance travelled in kilometers")
    mode = models.CharField(
        max_length=50,
        choices=[
            ('public', 'Public'),
            ('private', 'Private'),
        ]
    )
    vehicle_size = models.CharField(
        max_length=50,
        choices=[
            ('small', 'Small'),
            ('average', 'Average'),
            ('large', 'Large'),
            ('big', 'Big'),
        ],
        help_text="Size category of the vehicle"
    )
    emissions = models.FloatField(help_text="CO₂ emissions in grams", blank=True, null=True)

    def calculate_emissions(self):
        """
        Calculate emissions based on vehicle type, size, and distance.
        """
        factor = EMISSION_FACTORS.get(self.vehicle_type, {}).get(self.vehicle_size, 0)
        self.emissions = factor * self.distance

    def save(self, *args, **kwargs):
        # Automatically calculate emissions before saving
        self.calculate_emissions()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transportation_Log: {self.vehicle_type} ({self.vehicle_size}) - {self.mode}"

# Emissions Summary Model
class EmissionsSummary(models.Model):
    total_distance = models.FloatField(default=0.0, help_text="Total distance traveled in kilometers")
    total_emissions = models.FloatField(default=0.0, help_text="Total CO₂ emissions in grams")

    def __str__(self):
        return f"Distance: {self.total_distance} km, Emissions: {self.total_emissions}"

    @classmethod
    def calculate_totals(cls):
        """
        Aggregate total distance and emissions from the Transportationmodel.
        """
        total_distance = Transportationmodel.objects.aggregate(Sum('distance'))['distance__sum'] or 0.0
        total_emissions = Transportationmodel.objects.aggregate(Sum('emissions'))['emissions__sum'] or 0.0

        summary, created = cls.objects.get_or_create(id=1)
        summary.total_distance = total_distance
        summary.total_emissions = total_emissions
        summary.save()

        return summary
Collapse
message.txt
3 KB
sizoo
Luffy — Today at 1:50 PM
++++++++++++++++++++++++++++++++++++++++++
Luffy — Today at 2:52 PM
from django.shortcuts import render
from core.models import Transportationmodel,EmissionsSummary
Create your views here.
def transportation_list(request):
    transportations = Transportationmodel.objects.all()

    context ={
        'transportations' : transportations
    }

    return render (request, 'core/transportation_list.html',context)
Aadityadav — Today at 5:13 PM
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages



Create your views here.
def Test(request):
    return HttpResponse("hello")



register user
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


#Dashboard for a user:
def dashboard(request):
    return render(request,'dashboard.html')





#logout a user:
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('login')
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages



Create your views here.
def Test(request):
    return HttpResponse("hello")



register user
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


#Dashboard for a user:
def dashboard(request):
    return render(request,'dashboard.html')





#logout a user:
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('login')
from django.urls import path
from .views import *


urlpatterns = [
     path('', register_user, name='register'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='Login'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),
path('profile/',views.user_profile, name='profile')
]
'DIRS': [BASE_DIR,"templates"],
Image
Aadityadav — Today at 5:21 PM
Image
Image
﻿
from django.db import models
from django.db.models import Sum

# Emission Factors (CO₂ in grams per kilometer)
EMISSION_FACTORS = {
    'car': {'small': 135, 'average': 165, 'large': 215, 'big': 300},
    'bike': {'small': 45, 'average': 60, 'large': 85},
    'scooter': {'small': 35, 'average': 45, 'large': 60},
    'bus': {'small': 30, 'average': 40, 'large': 55},
    'train': {'electric': 20, 'diesel': 55},
}

# Transportation Model
class Transportationmodel(models.Model):
    vehicle_type = models.CharField(
        max_length=50,
        choices=[
            ('car', 'Car'),
            ('bike', 'Bike'),
            ('bus', 'Bus'),
            ('scooter', 'Scooter'),
        ]
    )
    distance = models.FloatField(help_text="Distance travelled in kilometers")
    mode = models.CharField(
        max_length=50,
        choices=[
            ('public', 'Public'),
            ('private', 'Private'),
        ]
    )
    vehicle_size = models.CharField(
        max_length=50,
        choices=[
            ('small', 'Small'),
            ('average', 'Average'),
            ('large', 'Large'),
            ('big', 'Big'),
        ],
        help_text="Size category of the vehicle"
    )
    emissions = models.FloatField(help_text="CO₂ emissions in grams", blank=True, null=True)

    def calculate_emissions(self):
        """
        Calculate emissions based on vehicle type, size, and distance.
        """
        factor = EMISSION_FACTORS.get(self.vehicle_type, {}).get(self.vehicle_size, 0)
        self.emissions = factor * self.distance

    def save(self, *args, **kwargs):
        # Automatically calculate emissions before saving
        self.calculate_emissions()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transportation_Log: {self.vehicle_type} ({self.vehicle_size}) - {self.mode}"

# Emissions Summary Model
class EmissionsSummary(models.Model):
    total_distance = models.FloatField(default=0.0, help_text="Total distance traveled in kilometers")
    total_emissions = models.FloatField(default=0.0, help_text="Total CO₂ emissions in grams")

    def __str__(self):
        return f"Distance: {self.total_distance} km, Emissions: {self.total_emissions}"

    @classmethod
    def calculate_totals(cls):
        """
        Aggregate total distance and emissions from the Transportationmodel.
        """
        total_distance = Transportationmodel.objects.aggregate(Sum('distance'))['distance__sum'] or 0.0
        total_emissions = Transportationmodel.objects.aggregate(Sum('emissions'))['emissions__sum'] or 0.0

        summary, created = cls.objects.get_or_create(id=1)
        summary.total_distance = total_distance
        summary.total_emissions = total_emissions
        summary.save()

        return summary
message.txt
3 KB