from django.shortcuts import render

def metodospago(request):
    context = {}
    return render(request,'metodospago/metodospago.html',context)
