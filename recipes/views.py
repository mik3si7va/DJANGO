from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'mik3si7va'})

def contact(request):
    return render(request, 'recipes/contact.html')

def about(request):
    return HttpResponse("About the Recipes Application")


# Create your views here.

