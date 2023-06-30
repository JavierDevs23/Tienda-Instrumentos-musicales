from django.shortcuts import render

# Create your views here.
def registrarse(request):
    context = {}
    return render(request,'registrarse/registrarse.html',context)