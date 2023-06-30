from django.shortcuts import render

# Create your views here.
def terminosCondiciones(request):
    context = {}
    return render(request,'terminosCondiciones/terminosCondiciones.html',context)