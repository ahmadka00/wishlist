from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileUpdateForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {})
        
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registed successfuly")
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        
        else:
            form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form':form})

@login_required(login_url='login') 
def user_profile(request):
    update_profile = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user_form = UserProfileUpdateForm(request.POST, instance=update_profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('my_profile')  # Redirect back to the profile page

    else:
        user_form = UserProfileUpdateForm(instance=update_profile)

    return render(request, 'accounts/my_profile.html', {'user_form': user_form})
