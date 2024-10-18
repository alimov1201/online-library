from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from account.forms import CustomAuthenticationForm, CustomUserCreationForm

def register_page(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    context = {
        'form':form,
    }
    return render(request, 'register.html', context=context)

def login_page(request):
    form = CustomAuthenticationForm()
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'login.html', context=context)

def logout_function(request):
    logout(request)
    return redirect('login')