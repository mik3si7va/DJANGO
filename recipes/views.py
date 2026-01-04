from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

from utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context={'username': 'mik3si7va','recipes': [make_recipe() for _ in range(12)]})

def contact(request):
    return render(request, 'recipes/contact.html')

def about(request):
    return HttpResponse("About the Recipes Application")

def recipe_detail(request):
    return render(request, 'recipes/pages/recipe-view.html', context={'username': 'mik3si7va', 'recipe': make_recipe()})

# Create your views here.

