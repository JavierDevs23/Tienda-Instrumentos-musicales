from django.shortcuts import render

# Create your views here.
def PreguntasFrec(request):
    context = {}
    return render(request,'PreguntasFrec/PreguntasFrec.html',context)