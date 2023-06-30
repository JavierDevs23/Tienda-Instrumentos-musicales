from django.urls import path
from . import views

urlpatterns = [
    path('',views.terminosCondiciones,name ='terminosCondiciones'),
]