from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.urls import path
import recipes
from recipes.models import Recipe
from utils.recipes.factory import make_recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-created_at')[:12]
    
    # if not recipes:
    #     raise Http404("No recipes found at All.. 😿😢😭")
    
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes})

def category(request, cat):
    recipes = Recipe.objects.filter(is_published=True, category__id=cat).order_by('-created_at')[:12]
    
    # recipes = get_list_or_404(Recipe.objects.filter(is_published=True, category__id=cat).order_by('-created_at')[:12])
    
    if not recipes:
        raise Http404("No recipes found for this category.. 😿😢😭")
    
    cat_name = getattr(getattr(recipes.first(), 'category', None), 'name', 'Not Found')
    
    return render(request, 'recipes/pages/category.html', context={'recipes': recipes, 'title': cat_name})

def contact(request):
    return render(request, 'recipes/contact.html')

def about(request):
    return HttpResponse("About the Recipes Application")

def recipe_detail(request, id):
    try:
        recipe = Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
        recipe = None
    
    if not recipe or not recipe.is_published:
        raise Http404("No recipe found with that id.. 😿😢😭")
    
    return render(request, 'recipes/pages/recipe-view.html', context={ 'id': id, 'recipe': recipe,'is_detail_page': True})

# Create your views here.

