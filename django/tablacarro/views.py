from django.shortcuts import render

# Create your views here.
def tablacarro(request):
    context = {}
    return render(request,'tablacarro/tablacarro.html',context)