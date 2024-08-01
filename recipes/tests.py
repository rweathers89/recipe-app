from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name="Tea", 
                              ingredients="Water, Tea leaves, Sugar", 
                              cooking_time="5")
    
    def test_recipe_name(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field("name").verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, "name")
    
    def test_recipe_name_max_length(self):
           # Get a recipe object to test
           recipe = Recipe.objects.get(id=1)

           # Get the metadata for the 'name' field and use it to query its max_length
           max_length = recipe._meta.get_field("name").max_length

           # Compare the value to the expected result i.e. 120
           self.assertEqual(max_length, 120)

    def test_recipe_cooking_time_positive_integer(self):
         recipe = Recipe.objects.get(id=1)

         positive_integer = recipe._meta.get_field("cooking_time").verbose_name

         self.assertTrue(positive_integer )

    def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of book #1
       #and load the URL /books/list/1
       self.assertEqual(recipe.get_absolute_url(), '/recipes/1')