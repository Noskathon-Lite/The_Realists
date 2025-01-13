from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.calculator_view, name='calculator_view'),
]
