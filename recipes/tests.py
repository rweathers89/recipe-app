from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm
from django.urls import reverse

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name="Tea", 
                              ingredients="Water, Tea leaves, Sugar", 
                              cooking_time=5)
    
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

#class RecipeFormTest(TestCase):
    def test_form_redners_chart_type(self):
        # Get a form object to test
        form = RecipeSearchForm()

        # Access the field's verbose name directly from the form's fields
        chart_type_label = form.fields["chart_type"].label
        
        # Compare the value to the expected result
        self.assertEqual(chart_type_label, "Chart type")

        # Additionally, you can check the choices
        chart_type_choices = form.fields["chart_type"].choices
        self.assertEqual(chart_type_choices, [
            ("#1", "Bar chart"),
            ("#2", "Pie chart"),
            ("#3", "Line chart"),
        ])

    def test_login_protection(self):
        # Test login protection for list view
        response = self.client.get(reverse('recipes:recipes_list'))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login page
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('recipes:recipes_list')}")
        
        # Test login protection for detail view
       # response = self.client.get(reverse('recipes:recipes_detail')) #kwargs={'pk': self.recipes.pk}
        #self.assertNotEqual(response.status_code, 200)  # Should redirect to login page
       # self.assertRedirects(response, f"{reverse('login')}?next={reverse('recipes:recipes_detail')}") #kwargs={'pk': self.recipes.pk}




    