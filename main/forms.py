from django import forms
from django.forms import ModelForm
from .models import Wishlist, Wish

# class WishListForm(ModelForm):
#     model = Wishlist
#     fields = ['list_name', 'created_at', 'is_active']

#     def __init__(self, *args, **kwargs):
#         super(WishListForm, self).__init__(*args, **kwargs)
#         self.fields['list_name'].widget = forms.TextInput(attrs={
#             'class': 'form-control rounded-3',
#             'id': 'floatingInput',
#             'placeholder': 'Wish List Name',
#             'autocomplete': 'off',
#         }),
#         self.fields['created_at'].widget=forms.DateTimeField(),
#         self.fields['is_active'].widget = forms.HiddenInput(),
#         # self.field['is_active'].widget=forms.CheckboxInput(attrs={
#         #     'class':'form-check-input',
#         #     'id':'flexSwitchCheckChecked',
#         #     'placeholder': 'Wish List Name',
#         #     'autocomplete':'off',
#         # })


