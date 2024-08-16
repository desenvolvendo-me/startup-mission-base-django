from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, LoginForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


def custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email ou senha incorretos')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
