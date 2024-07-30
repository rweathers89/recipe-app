# src/recipes/urls.py
from django.urls import path
from .views import home

# specify the app_name
app_name = "recipes"

# specify the name of your FBV and pass it as the second argument to the path function
urlpatterns = [
    path("", home),
]