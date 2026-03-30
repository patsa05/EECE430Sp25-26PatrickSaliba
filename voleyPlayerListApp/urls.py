from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.view_players, name='player_list'),
    path('add/', views.add_player, name='add_player'),
    path('update/<int:player_id>/', views.update_player, name='update_player'),
    path('delete/<int:player_id>/', views.delete_player, name='delete_player'),
]