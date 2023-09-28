from typing import Any
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from main.models import Profile, Wish, Wishlist
from django.views import generic
from .forms import WishListForm, AddWishForm, AddImageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


"""
All function / classes will redirect to main:user_profile (in main app) after implementing success.
"""

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
        return reverse('main:user_profile', kwargs={'username': self.request.user.username})

class DeleteWishList(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):

    model = Wishlist
    template_name = 'wishy/user_profile.html'


    def test_func(self):
        wish_list = self.get_object()
        return self.request.user == wish_list.user
    
    def get_success_url(self):
        # Redirect the user to their profile page with the correct 'username' parameter
        return reverse('main:user_profile', kwargs={'username': self.request.user.username})
    

# UserPassesTestMixin mixin Django come with test_func function in this casse the mixin check if the user allowed (the owner of the list) to update or delete or give access denied 
class UpdateWishList(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):

    model = Wishlist
    form_class = WishListForm
    template_name = 'wishy/update_list.html'
    template_name_suffix = '_form'

    def test_func(self):
        wish_list = self.get_object()
        return self.request.user == wish_list.user
    

    def get_success_url(self):
        # After successful form submission, redirect to user's profile
        return reverse('wishy:user_profile', kwargs={'username': self.request.user.username})
    

class CreateWishView(LoginRequiredMixin, generic.CreateView):
    model = Wish
    form_class = AddWishForm
    template_name = 'wishy/add_wish.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the user's active wish lists
        context['wish_lists'] = Wishlist.objects.filter(user=self.request.user, is_active=True)

        context['image'] = AddImageForm()
        return context


    def form_valid(self, form):
        
        wish = form.save(commit=False)
        # Set the wish's list based on the user's choice
        selected_wish_list_pk = self.request.POST['wish_list']
        wish.list_name = Wishlist.objects.get(pk=selected_wish_list_pk)


        # Handle image upload from AddImageForm
        image_form = AddImageForm(self.request.POST, self.request.FILES)

        if image_form.is_valid():
            wish.image = image_form.cleaned_data['image']

        wish.save()


        return super().form_valid(form)
    
    def get_success_url(self):
        # After successful form submission, redirect to user's profile
        return reverse('main:user_profile', kwargs={'username': self.request.user.username})


class DeleteWish(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):

    model = Wish
    template_name = 'wishy/user_profile.html'


    def get_queryset(self):
        # Ensure that only the wishes owned by the currently logged-in user can be deleted
        return self.model.objects.filter(list_name__user=self.request.user)
    
    def test_func(self):
        # Check if the user is logged in and has the necessary permissions
        return self.request.user.is_authenticated
    
    def get_success_url(self):
        # Redirect the user to their profile page with the correct 'username' parameter
        return reverse('main:user_profile', kwargs={'username': self.request.user.username})

    def handle_no_permission(self):
        # Handle the case when the user is not logged in
        return super().handle_no_permission()
    

 # UserPassesTestMixin mixin Django come with test_func function in this casse the mixin check if the user allowed (the owner of the list) to update or delete or give access denied 
class UpdateWish(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):

    model = Wish
    form_class = AddWishForm
    template_name = 'wishy/update_wish.html'

    def test_func(self):
        wish = self.get_object()
        return self.request.user == wish.list_name.user
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        wish = get_object_or_404(Wish, pk=pk)
        return wish

    
    def get_success_url(self):
        # After successful form submission, redirect to user's profile
        return reverse('main:user_profile', kwargs={'username': self.request.user.username})
       

class WishPageView(LoginRequiredMixin, generic.DetailView):
    model = Wish
    template_name = 'wishy/single_wish.html'
    context_object_name = 'wish'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        wish = get_object_or_404(Wish, pk=pk)
        return wish



