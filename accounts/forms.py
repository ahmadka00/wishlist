from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Username',
            'autocomplete': 'off',
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Email Address',
            'autocomplete': 'off',
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingPassword',
            'placeholder': 'Password',
            'autocomplete': 'off',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingPassword',
            'placeholder': 'Confirm Password',
            'autocomplete': 'off',
        })


class UserProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Username',
            'autocomplete': 'off',
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Email Address',
            'autocomplete': 'off',
        })


class UserPasswordChangeForm(PasswordChangeForm):

    model = User
    fields = ['old_password', 'new_password1', 'new_password2']
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingOldPassword',
            'placeholder': 'Old Password',
            'autocomplete': 'off',
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword1',
            'placeholder': 'New Password',
            'autocomplete': 'off',
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword2',
            'placeholder': 'Confirm New Password',
            'autocomplete': 'off',
        })


class UserPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Email Address',
            'autocomplete': 'off',
        })


class UserPasswordResetConfirmViewForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword1',
            'placeholder': 'New Password',
            'autocomplete': 'off',
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword2',
            'placeholder': 'Confirm New Password',
            'autocomplete': 'off',
        })

