from django.shortcuts import render, redirect
#Django authentication libraries           
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm 

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