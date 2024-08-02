from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

#class-based view
class RecipeListView(LoginRequiredMixin, ListView):
   #specify model
   model = Recipe
   #specify template 
   template_name = "recipes/recipes_list.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
   #specify model
   model = Recipe
   #specify template 
   template_name = "recipes/recipes_detail.html"

#To protect function-based views add 
# @login_required before the defined function