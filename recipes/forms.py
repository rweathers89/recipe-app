# src/recipes/forms.py
from django import forms
from .models import Recipe

#specify choices as a tuple
CHART__CHOICES = (
    ("#1", "Bar chart"),
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)


#define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices = CHART__CHOICES, label="Chart type")

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=200, required=False, label="Search Recipes")
    # ingredients = forms.CharField(max_length=200, required=False, label="Ingredients")
    show_all = forms.BooleanField(required=False)

class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "cooking_time", "difficulty", "ingredients", "pic"]


'''
DIFFICULTY__CHOICES = (
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Intermediate", "Intermediate"),
    ("Hard", "Hard"),
)

# define class-based Form imported from Django forms
class DifficultySearchForm(forms.Form):
    recipe_difficulty = forms.ChoiceField(choices=DIFFICULTY__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
'''