from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('core.urls')),
=======
    path('', include('auth_app.urls')), 
>>>>>>> nirbhay
]
