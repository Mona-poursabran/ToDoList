from turtle import home
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('edit/<int:item_id>/', edit_item, name= 'update'),
    path('delete/', delete_item, name='delete_item'),
    path('delete-all/', delete_all, name= 'delete_all'),
    path('delete_completed', delete_completed, name="delete_completed"),
    path('cross-off/<int:item_id>/', cross_off, name= 'cross_off'),
    path('uncross/<int:item_id>/', uncross, name='uncross'),
]
