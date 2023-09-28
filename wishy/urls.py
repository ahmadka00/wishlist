from django.urls import path
from . import views


app_name = 'wishy'

urlpatterns = [
    # path('@<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
    path('@<str:username>/add_list/', views.CreateWishListView.as_view(), name='add_list'),
    path('@<str:username>/delete_list/<int:pk>/', views.DeleteWishList.as_view(), name='delete_list'),
    path('@<str:username>/update_list/<int:pk>/', views.UpdateWishList.as_view(), name='update_list'),
    path('@<str:username>/add_wish', views.CreateWishView.as_view(), name='add_wish'),
    path('@<str:username>/wishes/<int:pk>', views.WishPageView.as_view(), name='show_wish'),
    path('@<str:username>/delete_wish/<int:pk>/', views.DeleteWish.as_view(), name='delete_wish'),
    path('@<str:username>/update_wish/<int:pk>/', views.UpdateWish.as_view(), name='update_wish'),
]
