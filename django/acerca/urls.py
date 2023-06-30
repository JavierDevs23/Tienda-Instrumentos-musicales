from django.urls import path
from . import views

urlpatterns = [
    path('',views.acerca,name ='acerca'),
]