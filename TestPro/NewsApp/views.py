from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def News(request):
    return HttpResponse("<h1> This is our latest News </h1>")
