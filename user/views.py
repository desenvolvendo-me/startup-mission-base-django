from django.shortcuts import render


def home(request):
    return render(request, 'teste_home.html')