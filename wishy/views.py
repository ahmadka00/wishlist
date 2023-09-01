from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Profile, Wish, Wishlist
from django.views import generic
from .forms import WishListForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'wishy/user_profile.html'
    context_object_name = 'profile'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
    redirect_field_name = "accounts/login"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['profile'].user
        wish_list = Wishlist.objects.filter(user=user)
        context['wish_list'] = wish_list
        context['username'] = user.username
        return context



class CreateWishListView(LoginRequiredMixin, generic.CreateView):
    model = Wishlist
    form_class = WishListForm
    template_name = 'wishy/add_list.html'
    redirect_field_name = "accounts/login"

    def form_valid(self, form):
        wish_list = form.save(commit=False)
        wish_list.user = self.request.user
        wish_list.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        # After successful form submission, redirect to user's profile
        return reverse('wishy:user_profile', kwargs={'username': self.request.user.username})

class DeleteWishList(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):
    model = Wishlist
    template_name = 'wishy/user_profile.html'


    def test_func(self):
        wish_list = self.get_object()
        return self.request.user == wish_list.user
    
    def get_success_url(self):
        # Redirect the user to their profile page with the correct 'username' parameter
        return reverse('wishy:user_profile', kwargs={'username': self.request.user.username})
    

