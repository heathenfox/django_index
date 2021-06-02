
from typing import ValuesView
from django.urls import path
from . import views
from calc.views import home 
urlpatterns = [ 
    path('', views.home , name= 'home')
]