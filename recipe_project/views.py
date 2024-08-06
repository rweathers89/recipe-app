from django.shortcuts import render, redirect
#Django authentication libraries           
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm 
from recipes.forms import SearchForm
from recipes.models import Recipe
import matplotlib.pyplot as plt
from django.conf import settings
import os
import io
import urllib, base64

def login_view(request):
    #initialize:                               
    error_message = None   
    #form object with username and password fields                             
    form = AuthenticationForm() 

    if request.method == 'POST':       
        #read the data sent by the form via POST request                   
        form =AuthenticationForm(data=request.POST)

            #check if form is valid
        if form.is_valid():                                
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #use Django authenticate function to validate the user
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)                
                return redirect('recipes:recipes_list')
        else:
            error_message ='ooops.. something went wrong'
    context ={  
         #send the form data and the error_message                                 
       'form': form,                                
       'error_message': error_message
    }
    #load the login page using "context" information
    return render(request, 'auth/login.html', context)    

def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')

def generate_plots():
    fig, ax = plt.subplots()
    ax.bar(...)  # Fill in with your data
    fig.savefig(os.path.join(settings.STATIC_ROOT, 'bar_plot.png'))

    fig, ax = plt.subplots()
    ax.pie(...)  # Fill in with your data
    fig.savefig(os.path.join(settings.STATIC_ROOT, 'pie_plot.png'))

    fig, ax = plt.subplots()
    ax.plot(...)  # Fill in with your data
    fig.savefig(os.path.join(settings.STATIC_ROOT, 'line_plot.png'))

def process_search_form(form):
    return Recipe.objects.filter(name__icontains=form.cleaned_data.get('search_term')) 

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            results = process_search_form(form)
            
            return render(request, 'search.html', {
                'form': form, 
                'results': results,
                'bar_plot': 'bar_plot.png',
                'pie_plot': 'pie_plot.png',
                'line_plot': 'line_plot.png',
            })
    else:
        form = SearchForm()
   
        return render(request, 'search.html', {'form': form})
    
def plot_view(request):
    generate_plots()  # This will generate the plot image
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)
    image_url = urllib.parse.quote(base64.b64encode(image.read()))
    return render(request, 'search.html', {'image_url': image_url})