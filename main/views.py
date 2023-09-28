from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Wish, Wishlist
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
import markdown


def home(request):
      if request.user.is_authenticated:
        username = request.user.username   
        return redirect('main:user_profile', username=username)
      else:
        readme_file_path = 'main/README.md'

        with open(readme_file_path, 'r') as readme_file:
            readme_content = readme_file.read()
            readme_html = markdown.markdown(readme_content)

        return render(request, 'main/home.html', {'readme_html': readme_html})


class UserProfileView(LoginRequiredMixin, generic.DetailView):

    model = Profile
    template_name = 'main/user_profile.html'
    context_object_name = 'profile'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
    redirect_field_name = "accounts/login"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['profile'].user
        wish_lists = Wishlist.objects.filter(user=user)
        wishes = Wish.objects.filter(list_name__in=wish_lists)
        persons = Profile.objects.exclude(user=self.request.user).prefetch_related('follows', 'followed_by')
        context['wish_lists'] = wish_lists
        context['wishes'] = wishes
        context['username'] = user.username
        context['persons'] = persons
        return context
        


@login_required(login_url='accounts:login')
def people(request):
    profile = request.user.profile
    persons = Profile.objects.exclude(user=request.user).prefetch_related('follows', 'followed_by')
    return render(request, 'main/people.html', {'persons': persons, 'profile': profile})


@login_required(login_url='accounts:login')
def friend_page(request, username):
    
    profile = get_object_or_404(Profile, user__username=username)
    if request.user == profile.user:
        return redirect('main:home')
    else:
        if request.method == 'POST':
            current_user_profile = request.user.profile
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # Save the profile
            current_user_profile.save() 

        followed_user = request.user.profile.follows.all().values_list('user', flat=True)
        wish_lists = Wishlist.objects.filter(user__in=followed_user)
        wishes = Wish.objects.filter(list_name__in=wish_lists)
        context = {'profile': profile,
                    'wish_lists': wish_lists, 
                    'wishes':wishes,
                    'username': profile.user.username,
                    }
        return render(request, 'main/friend_page.html', context)







"""
Another function Idea to retrive followers and followed_by
"""

# @login_required(login_url='accounts:login')
# def people(request):
#     persons =  Profile.objects.exclude(user=request.user)    
#     profile = request.user.profile
#     # Retrive followers of the user 
#     follows = profile.follows.all()
#     # Retrive Follow_by the user
#     followed = profile.followed_by.all()

#     return render(request, 'main/people.html', {'persons': persons, 'follows':follows, 'followed':followed})
