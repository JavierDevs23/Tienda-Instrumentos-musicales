from django.shortcuts import render

# Create your views here.
def ingresar(request):
    context = {}
    return render(request,'ingresar/ingresar.html',context)
