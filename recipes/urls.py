# src/recipes/urls.py
from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, search_view

# specify the app_name
app_name = "recipes"

# specify the name of your FBV and pass it as the second argument to the path function
urlpatterns = [
    path("", home),
    path('recipes/', RecipeListView.as_view(), name='recipes_list'),
    path('recipes/<pk>', RecipeDetailView.as_view(), name='recipes_detail'),
    path('search/', search_view, name='recipes_search')
]