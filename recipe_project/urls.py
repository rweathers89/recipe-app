# src/recipe_project/urls.py

"""
URL configuration for recipe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# include package will allow you to use the include() function that will link the urls.py
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, logout_view, search_view
from recipes.views import create_view
from recipes.views import recipes_home

urlpatterns = [
    path('admin/', admin.site.urls),
    # The empty quotes '' indicate that this path refers to the home page
    path('', include('recipes.urls')),
    #path("recipes/", include("recipes.urls")),
    # add login path
    path('login/', login_view, name='login'),
    path("", recipes_home, name="home"),
    path('success/', logout_view, name='success'),
    # add search path
    path('search/', search_view, name='search'),
    path('create/', create_view, name='create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
