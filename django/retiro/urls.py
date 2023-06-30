from django.urls import path
from . import views

urlpatterns = [
    path('',views.retiro,name ='retiro'),
]