from django.shortcuts import render, redirect
from .models import Profile, Wish, Wishlist
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views import generic
# from .forms import WishListForm
# from django.views.generic.edit import CreateView
# from django.utils.decorators import method_decorator


def home(request):
      if request.user.is_authenticated:
        username = request.user.username   
        return redirect('wishy:user_profile', username=username)
      else:
         return render(request, 'main/home.html')

        
@login_required(login_url='accounts:login')
def people(request):
        persons =  Profile.objects.exclude(user=request.user)
        return render(request, 'main/people.html', {'persons':persons})


