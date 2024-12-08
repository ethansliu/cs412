from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path(url, view, name)
    path(r'', views.ShowHomeView.as_view(), name="home_page"), 
    path(r'profile/<int:pk>', views.ShowClosetView.as_view(), name="show_closet"),
    path(r'closet/<int:pk>', views.ShowCategoryView.as_view(), name="show_category"), 
    path(r'clothes/<int:pk>', views.ShowClothesView.as_view(), name="show_clothes"), 

    path(r'closet/<int:pk>/add_category/', views.CreateCategoryView.as_view(), name="create_category"), 
    path(r'closet/<int:pk>/update_category', views.UpdateCategoryView.as_view(), name="update_category"), 
    path(r'closet/<int:pk>/delete_category', views.DeleteCategoryView.as_view(), name="delete_category"), 

    path(r'closet/<int:pk>/add_clothes/', views.CreateClothesView.as_view(), name="create_clothes"),
    path(r'clothes/<int:pk>/update/', views.UpdateClothesView.as_view(), name="update_clothes"),
    path(r'clothes/<int:pk>/delete/', views.DeleteClothesView.as_view(), name="delete_clothes"),

    path(r'sell', views.ShowSellClothesView.as_view(), name="sell_clothes"),

    path(r'sell/add_sell/', views.CreateSellClothesView.as_view(), name="add_sell"),
    path(r'sell/<int:pk>/update_sell/', views.UpdateSellClothesView.as_view(), name="update_sell"),
    path(r'sell/<int:pk>/delete_sell/', views.DeleteSellClothesView.as_view(), name="delete_sell"),

    path(r'outfit/add/', views.CreateOutfitView.as_view(), name='add_outfit'),
    path(r'outfit/<int:pk>/update/', views.UpdateOutfitView.as_view(), name='update_outfit'),
    path(r'outfit/<int:pk>/delete/', views.DeleteOutfitView.as_view(), name='delete_outfit'),
    path(r'outfits/', views.ShowOutfitView.as_view(), name='show_outfits'),
    path(r'outfits/<int:pk>', views.ShowOutfitDetailView.as_view(), name='show_outfit_detail'),
]