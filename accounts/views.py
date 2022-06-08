from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout, login
from permissions import UserNotLoginMixin


class UserLoginView(UserNotLoginMixin, View):
    template_name = 'accounts/login.html'
    class_form = UserLoginForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.class_form(request=request)})

    def post(self, request):
        form = self.class_form(request=request, data=request.POST)
        if form.is_valid():
            messages.success(request, "you're logged in successfully")
            return redirect('core:home')
        return render(request, self.template_name, {"form": form})


class UserRegisterView(UserNotLoginMixin, View):
    template_name = 'accounts/register.html'
    class_form = UserRegisterForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.class_form()})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            instance = form.save()
            login(request, instance)
            messages.success(request, "you are registered successfully")
            return redirect('core:home')
        return render(request, self.template_name, {"form": form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you are logged out successfully')
        return redirect('accounts:login')
