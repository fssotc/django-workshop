from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
method 1 :
def index(request):
    return HttpResponse('<h1> hello </h1>
    <button> send </button>
    ')
"""    
# method 2 : 
def index(request):
    return render(request,'display/index.html')
