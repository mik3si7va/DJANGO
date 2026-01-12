from recipes.models import Recipe, User
from recipes.tests.test_recipe_views import RecipeTestBase
from parameterized import parameterized


class RecipeModelsTest(RecipeTestBase):
    def setUp(self):
        return super().setUp()

    def test_recipe_exists(self):
        """Recipe must exist"""
        self.assertTrue(Recipe.objects.exists())
        
    def test_user_exists(self):
        """Author (User) must exist"""
        self.assertTrue(User.objects.exists())
        
    @parameterized.expand([
        ('title', 'Recipe 1'),  
        ('description', 'Recipe description'),
        ('slug', 'recipe-1'),
        ('preparation_time', 10),
        ('servings', 2),
        ('preparation_steps', 'Do the thing'),
        ('is_published', False),
    ])
    
    def test_recipe_fields(self, field_name, expected_value):
        """Test specific fields of the Recipe model"""
        recipe = Recipe.objects.first()
        actual_value = getattr(recipe, field_name)
        self.assertEqual(actual_value, expected_value)
        
    def test_recipe_prep_steps_is_hmtl_is_false_by_default(self):
        """Test that preparation steps is_html defaults to False"""
        recipe = Recipe.objects.first()
        self.assertFalse(recipe.preparation_steps_is_html)
    
    def test_recipe_is_published_is_false_by_default(self):
        """Test that is_published defaults to False"""
        recipe = Recipe.objects.first()
        self.assertFalse(recipe.is_published)
        
    def test_recipe_string_representation(self):
        """Test the string representation of the Recipe model"""
        recipe = Recipe.objects.first()
        self.assertEqual(str(recipe), recipe.title)
        
    def test_category_string_representation(self):
        """Test the string representation of the Category model"""
        category = self.make_category(name='Desserts')
        self.assertEqual(str(category), 'Desserts')