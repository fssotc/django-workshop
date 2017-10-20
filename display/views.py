from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, name):
    print(name)
    return HttpResponse('hello '+name)
"""    
# method 2 : 
def index(request):
    return render(request,'display/index.html')
"""
