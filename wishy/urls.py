from django.urls import path
from . import views


app_name = 'wishy'

urlpatterns = [
    path('@<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
    path('@<str:username>/add_list/', views.CreateWishListView.as_view(), name='add_list'),
    path('@<str:username>/delete_list/<int:pk>/', views.DeleteWishList.as_view(), name='delete_list'),

]
