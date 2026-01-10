from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from unittest import skip

from recipes.models import Category, Recipe

from recipes.views import *
class RecipeTestBase (TestCase):
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        username='user1',
        password='pass1234',
        first_name='First',
        last_name='Last',
    ):
        return User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        
    def make_recipe(self):
        return Recipe.objects.create(
            title='Recipe 1',
            description='Recipe description',
            slug='recipe-1',
            preparation_time=10,
            servings=2,
            preparation_steps='Do the thing',
            is_published=True,
            category=self.category,
            author=self.user,
        )
    def setUp(self):
        self.category = self.make_category()
        self.user = self.make_author()
        self.recipe = self.make_recipe()

class RecipeViewsTest(RecipeTestBase):
    
    
    @skip("Demonstration of skip decorator")
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', kwargs={'id': self.recipe.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    def test_home_view_resolve(self):
        url = resolve('/')
        self.assertEqual(url.view_name, 'home')
        
    def test_recipe_detail_view_resolve(self):
        url = resolve(f'/recipe/{self.recipe.id}/')
        self.assertEqual(url.view_name, 'recipe_detail')
    
    def test_category_view_resolve(self):
        url = resolve(f'/category/{self.category.id}/')
        self.assertEqual(url.view_name, 'category')
    
    def test_home_view_way_2(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func, home)

    def test_recipe_detail_view_way_2(self):
        view = resolve(reverse('recipe_detail', kwargs={'id': 7}))
        self.assertEqual(view.func, recipe_detail)