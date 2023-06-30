from django.urls import path
from . import views

urlpatterns = [
    path('',views.registrarse,name ='registrarse'),
]