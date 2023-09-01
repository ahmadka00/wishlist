from django.shortcuts import redirect
from .forms import CustomUserCreationForm, UserProfileUpdateForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Profile, Wish, Wishlist



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('main:home')


    def dispatch (self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:home')
        return super().dispatch(request, *args, **kwargs)
  
class RegisterView(generic.CreateView, LoginRequiredMixin):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('main:home')
    
    
    def dispatch (self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return response


class UserProfileUpdate(generic.UpdateView, LoginRequiredMixin):
    model = User
    form_class = UserProfileUpdateForm
    template_name = 'accounts/my_profile.html'
    success_url = reverse_lazy('accounts:my_profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    
class UserPasswordChange(PasswordChangeView, LoginRequiredMixin):
    model = User
    form_class = UserPasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('main:home')



