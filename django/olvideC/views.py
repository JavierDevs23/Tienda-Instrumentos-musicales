from django.shortcuts import render

# Create your views here.
def olvideC(request):
    context = {}
    return render(request,'olvideC/olvideC.html',context)