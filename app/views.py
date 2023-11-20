from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'a':'MAMATHA'}
    return render(request,'forloop.html',d)