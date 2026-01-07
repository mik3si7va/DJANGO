from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=77)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=77)
    description = models.TextField(max_length=250)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField() # in minutes
    preparation_time_unit = models.CharField(max_length=20, default='Minutes')
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=20, default='Portions')
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title