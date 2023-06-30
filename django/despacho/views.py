from django.shortcuts import render

# Create your views here.
def despacho(request):
    context = {}
    return render(request,'despacho/despacho.html',context)