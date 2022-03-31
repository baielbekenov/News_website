from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('elements/', index2, name='elements'),
    path('detail/<int:pk>/', DetailBookView.as_view(), name='detail'),
    path('generic/', CreateBookView.as_view(), name='generic'),
    path('elements/', Elements.as_view(), name='elements'),
    path('list_categories/', list_category, name='generic'),
    # path('list_category/', List_category.as_view(), name='list_category'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('posts_detail/<int:pk>/', PostDetailView.as_view(), name='posts_detail'),
    path('list_category/<int:pk>/', ListCategory.as_view(), name='list_category'),

]