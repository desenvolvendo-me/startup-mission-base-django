from django.shortcuts import render

def home(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')

def dashboard_view(request):
    return render(request, 'pages/dashboard.html')