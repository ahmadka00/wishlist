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


admin.site.register(Wishlist)


admin.site.register(Wish)


# class PortfolioAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'list_slug': ('list_name',), 'wish_slug' : ('wish_name',),}


# # Register Wishlist
# @admin.register(Wishlist)
# class WishListAdmin(admin.ModelAdmin):
#     list_display = ['list_name', 'list_slug']
#     prepopulated_fields = {'list_slug': ('list_name',)}

# # Register Wish
# @admin.register(Wish)
# class WishAdmin(admin.ModelAdmin):
#     list_display = ['wish_name', 'wish_slug']
#     prepopulated_fields = {'wish_slug': ('wish_name',)}