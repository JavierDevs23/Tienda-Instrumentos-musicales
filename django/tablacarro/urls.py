from django.urls import path
from . import views

urlpatterns = [
    path('',views.tablacarro,name ='tablacarro'),
]