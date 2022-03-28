from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', DetailBookView.as_view(), name='detail'),
    path('generic/<int:pk>/', CreateBookView.as_view(), name='generic'),
]