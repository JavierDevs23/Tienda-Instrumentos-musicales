from django.urls import path
from . import views

urlpatterns = [
    path('',views.despacho,name ='despacho'),
]