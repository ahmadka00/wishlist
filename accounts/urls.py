from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import UserPasswordResetForm, UserPasswordResetConfirmViewForm
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(next_page='main:home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='main:home'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register_user'),
    path('profile/', views.UserProfileUpdate.as_view(), name='my_profile'),
    path('change_password/', views.UserPasswordChange.as_view(), name='change_password'), 

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset/password_reset.html", 
                                                                 form_class=UserPasswordResetForm, success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),

    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset/password_reset_done.html"), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset/password_reset_confirm.html", 
                                                                 form_class=UserPasswordResetConfirmViewForm, success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset/password_reset_complete.html"), name='password_reset_complete'),

]