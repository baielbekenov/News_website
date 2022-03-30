from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', DetailBookView.as_view(), name='detail'),
    path('generic/', CreateBookView.as_view(), name='generic'),
    path('elements/', Elements.as_view(), name='elements')
]