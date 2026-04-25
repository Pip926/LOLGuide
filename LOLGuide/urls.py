from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('champions/', views.champions_list, name='champions_list'),
    path('champion/<int:pk>/', views.champion_detail, name='champion_detail'),
    path('authorization/', views.auth_view, name='authorization'),
    path('profile/', views.profile_view, name='profile'),
    path('regions/', views.regions_list, name='regions_list'),
    path('region/<int:pk>/', views.region_detail, name='region_detail'),
    path('items/', views.items_list, name='items_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('monsters/', views.monsters_hub, name='monsters_hub'),
    path('monsters/common/', views.common_monsters_list, name='common_monsters_list'),
    path('monsters/common/<int:pk>', views.monster_detail, name='monster_detail'),
    path('monsters/bosses/', views.boss_monsters_list, name='boss_monsters_list'),
    path('monster/bosses/<int:pk>/', views.boss_detail, name='boss_detail'),
]
