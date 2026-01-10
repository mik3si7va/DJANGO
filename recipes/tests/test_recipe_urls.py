from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from recipes.models import Category, Recipe

from recipes.views import *


class RecipeURLsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass1234')
        self.category = Category.objects.create(name='Category 1')
        self.recipe = Recipe.objects.create(
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

    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_url(self):
        response = self.client.get(f'/recipe/{self.recipe.id}/')
        self.assertEqual(response.status_code, 200)
   
    def test_category_url_reverse(self):
        url = reverse('recipe_detail', kwargs={'id': 7})
        self.assertEqual(url, '/recipes/7/')
   
    def test_category_url(self):
        response = self.client.get(f'/category/{self.category.id}/')
        self.assertEqual(response.status_code, 200)

    def test_category_url_reverse(self):
        url = reverse('category', kwargs={'cat': 7})
        self.assertEqual(url, '/category/7/')

    def test_contact_url(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)