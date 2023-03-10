from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import index
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_item', add_item, name='add_item'),
    path('delete_item/<int:myid>/', delete_item, name='delete_item'),
]
