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

class AddWishForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['wish_name', 'description', 'link']

    def __init__(self, *args, **kwargs):
        super(AddWishForm, self).__init__(*args, **kwargs)
        self.fields['wish_name'].widget = forms.TextInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'wish_name_floatingInput',
            'placeholder': 'Wish Name',
            'autocomplete': 'off',
        })
        self.fields['description'].widget = forms.TextInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'description_floatingInput',
            'placeholder': 'Description of the wish',
            'autocomplete': 'off',
        })
        self.fields['link'].widget = forms.URLInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'link_floatingInput',
            'placeholder': 'Link of the wish',
            'autocomplete': 'off',
        })


class AddImageForm(forms.ModelForm):
    image = forms.ImageField(label="Image", required=False)

    class Meta:
        model = Wish
        fields = ('image',)

