from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> Django -> response
#request handler

def say_hello(request):
    #return HttpResponse('Hello World!')
    return HttpResponse('Hello World!')