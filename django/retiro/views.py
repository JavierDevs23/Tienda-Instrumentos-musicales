from django.shortcuts import render

# Create your views here.
def retiro(request):
    context = {}
    return render(request,'retiro/retiro.html',context)