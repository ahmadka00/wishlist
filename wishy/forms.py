from django import forms
from main.models import Wishlist, Wish

class WishListForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['list_name']

    # def __init__(self, *args, **kwargs):
    #     super(WishListForm, self).__init__(*args, **kwargs)
    #     self.fields['list_name'].widget = forms.TextInput(attrs={
    #         'class': 'form-control rounded-3',
    #         'id': 'floatingInput',
    #         'placeholder': 'Wish List Name',
    #         'autocomplete': 'off',
    #     }),
        # self.fields['created_at'].widget=forms.DateTimeField(),
        # self.fields['is_active'].widget = forms.HiddenInput(),
