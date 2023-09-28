from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('@<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
    path('people/', views.people, name='people'),
    path('people/@<str:username>/', views.friend_page, name='friend')
        
]
