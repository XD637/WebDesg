from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm



def sign_in(response):
    if response.method == 'GET':
        form = LoginForm()
        return render(response, 'users/login.html', {'form': form})
    elif response.method == 'POST':
        form = LoginForm(response.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response,username=username,password=password)
            if user:
                login(response, user)
                messages.success(response,f'Hi {username.title()}, welcome back!')
                return redirect('/')
        
        # form is not valid or user is not authenticated
        messages.error(response,f'Invalid username or password')
        return render(response,'users/login.html',{'form': form})
