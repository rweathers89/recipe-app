from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

#class-based view
class RecipeListView(ListView):
   #specify model
   model = Recipe
   #specify template 
   template_name = "recipes/recipes_list.html"

class RecipeDetailView(DetailView):
   #specify model
   model = Recipe
   #specify template 
   template_name = "recipes/recipes_detail.html"