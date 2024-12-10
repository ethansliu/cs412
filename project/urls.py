from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Home page path
    path(r'', views.ShowHomeView.as_view(), name="home_page"),

    # Closet paths
    path(r'create_closet', views.CreateClosetView.as_view(), name="create_closet"),
    path(r'profile/<int:pk>', views.ShowClosetView.as_view(), name="show_closet"),
    path(r'profile/update_closet', views.UpdateClosetView.as_view(), name="update_closet"),
    path(r'closet/<int:pk>', views.ShowCategoryView.as_view(), name="show_category"), 
    path(r'clothes/<int:pk>', views.ShowClothesView.as_view(), name="show_clothes"), 

    # Category paths
    path(r'closet/<int:pk>/add_category/', views.CreateCategoryView.as_view(), name="create_category"), 
    path(r'closet/<int:pk>/update_category', views.UpdateCategoryView.as_view(), name="update_category"), 
    path(r'closet/<int:pk>/delete_category', views.DeleteCategoryView.as_view(), name="delete_category"), 

    # Clothes paths
    path(r'closet/<int:pk>/add_clothes/', views.CreateClothesView.as_view(), name="create_clothes"),
    path(r'clothes/<int:pk>/update/', views.UpdateClothesView.as_view(), name="update_clothes"),
    path(r'clothes/<int:pk>/delete/', views.DeleteClothesView.as_view(), name="delete_clothes"),

    # Sell paths
    path(r'sell', views.ShowSellClothesView.as_view(), name="sell_clothes"),
    path(r'sell/add_sell/', views.CreateSellClothesView.as_view(), name="add_sell"),
    path(r'sell/<int:pk>/update_sell/', views.UpdateSellClothesView.as_view(), name="update_sell"),
    path(r'sell/<int:pk>/delete_sell/', views.DeleteSellClothesView.as_view(), name="delete_sell"),

    # Outfit paths
    path(r'outfit/add/', views.CreateOutfitView.as_view(), name='add_outfit'),
    path(r'outfit/<int:pk>/update/', views.UpdateOutfitView.as_view(), name='update_outfit'),
    path(r'outfit/<int:pk>/delete/', views.DeleteOutfitView.as_view(), name='delete_outfit'),
    path(r'outfits/', views.ShowOutfitView.as_view(), name='show_outfits'),
    path(r'outfits/<int:pk>', views.ShowOutfitDetailView.as_view(), name='show_outfit_detail'),

    # Login/logout paths
    path(r'login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'), 
    path(r'logout/', auth_views.LogoutView.as_view(template_name='project/logout.html'), name='logout'),
]