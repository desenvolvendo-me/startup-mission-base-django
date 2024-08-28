from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, FormView
from .forms import CustomUserCreationForm, LoginForm
from .permissions import UserIsOwnerMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'teste_home.html'


class SignupView(FormView):
    template_name = 'teste_signup.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(FormView):
    template_name = 'teste_login.html'
    form_class = LoginForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, 'Email ou senha incorretos')
            return self.form_invalid(form)
