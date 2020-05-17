from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Bloglist.as_view(), name='home'),
    path('details/<str:pk>', BlogDetail.as_view(), name='detail'),
    path('update/<str:pk>', BlogUpdate.as_view(), name='update'),
    path('addpost/', BlogCreate.as_view(), name='addpost' ),
    path('delete/<str:pk>', BlogDelete.as_view(), name='deletepost'),
    path('category/', CategoryCreate.as_view(), name='category'),
    path('cats/<str:cats>/', CategoryView, name='cats'),
    path('like/<int:pk>', LikeView, name='like_post')
   
   
    
    
]
