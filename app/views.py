from django.shortcuts import render

# Create your views here.

def forloop(request):
    d={'NAME':'Balaji'}
    return render(request,'forloop.html',d)