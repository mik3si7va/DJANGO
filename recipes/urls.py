from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('category/<int:cat>/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
