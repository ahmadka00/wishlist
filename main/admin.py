from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Wishlist, Wish




# Mix profile info into User info
class ProfileInLine(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on admin page
    fields = ['username']
    inlines = [ProfileInLine]


# Unregister Initial User
admin.site.unregister(User)

# Register User and Profile
admin.site.register(User, UserAdmin)

# Register Wishlist
admin.site.register(Wishlist)

# Register Wish
admin.site.register(Wish)
