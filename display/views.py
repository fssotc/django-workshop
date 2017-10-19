from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello')
"""    
# method 2 : 
def index(request):
    return render(request,'display/index.html')
"""
