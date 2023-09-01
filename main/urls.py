from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('people/', views.people, name='people'),
     
    # path('create_wish_list/', views.CreateWishListView.as_view()),    
]
