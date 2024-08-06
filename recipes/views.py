from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm, SearchForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart

# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

#class-based view
class RecipeListView(LoginRequiredMixin, ListView):
   #specify model
   model = Recipe
   #specify template 
   template_name = "recipes/recipes_list.html"

   context_object_name = 'recipes'
   ordering = ['name']

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = SearchForm()
      return context
   def post(self, request, *args, **kwargs):
      form = SearchForm(request.POST)
      if not form.is_valid():
         return super().get(request, *args, **kwargs)

      name_query = form.cleaned_data['search_term']
      self.object_list = self.model.objects.filter(name__icontains=name_query)
      context = self.get_context_data(object_list=self.object_list, form=form)
      return render(request, self.template_name, context)


class RecipeDetailView(LoginRequiredMixin, DetailView):
   #specify model
   model = Recipe
   #specify template 
   template_name = "recipes/recipes_detail.html"

   context_object_name = 'recipes_detail'
   ordering = ['name']

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = SearchForm()
      return context

#To protect function-based views add 
# @login_required before the defined function



def search_view(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    chart = None
    qs = None
    #check if button is clicked 
    if request.method == 'POST':
        #check chart type
        chart_type = request.POST.get('chart_type')

        qs = Recipe.objects.all()
        if qs:
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df,
                              labels=recipe_df['name'].values)

            recipe_df = recipe_df.to_html()
    #pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipe_df': recipe_df,
        'chart': chart,
        'qs': qs,
    }
    #load the recipes/search.html page using the data above
    return render(request, 'recipes/recipes_search.html', context)

'''

def get(self, request):
   form = RecipeSearchForm()
   recipes_df = Recipe.objects.all()
   return render(request, 'recipes/recipes_list.html', {'form': form, 'recipes_df': recipes_df})

def post(self, request):
   form = RecipeSearchForm(request.POST)
   recipes_df = Recipe.objects.all()
   chart = None

   if form.is_valid():
      recipe_name = form.cleaned_data.get('recipe_name')
      chart_type = form.cleaned_data.get('chart_type')

      qs =Recipe.objects.filter(name__icontains=recipe_name)
      if qs:
         #convert the queryset values to pandas dataframe
         recipes_df = pd.DataFrame(qs.values())
         #convert the ID to recipe name
         #recipes_df['recipes_id'] = recipes_df['recipes_id'].apply(get_recipename_from_id)
         #call get_chart by passing chart_type from user input, sales dataframe and labels
         chart = get_chart(chart_type, recipes_df, labels=recipes_df['id'].values)
         #convert the dataframe to HTML
         recipes_df = recipes_df.to_html()
      print (recipe_name, chart_type)

   print('Exploring querysets:')
   print('Case 1: Output of Recipe.objects.all()')
   qs=Recipe.objects.all()
   print(qs)
      
   print('Case 2: Output of Recipe.objects.filter(recipe__name=recipe_name)')
   qs = Recipe.objects.filter(name__icontains=recipe_name)
   print(qs)

   print('Case 3: Output of qs.values')
   print(qs.values())

   print('Case 4: Output of qs.values_list()')
   print(qs.values_list())

   print('Case 5: Output of Sale.objects.get(id=1)')
   obj = Recipe.objects.get(id=1)
   print(obj)

         #else:
          #  recipes = pd.DataFrame()
   context = {
            'form': form,
            'recipes_df': recipes_df,
            'chart': chart,
        }
   return render(request, 'recipes/recipes_list.html', context)
'''