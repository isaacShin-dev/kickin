from django.urls import path, include
from . import views

urlpatterns = [
    path('img/main/', views.main_img),
    path('sneaker/', views.get_sneaker),
    
    # urls for admin
    path('new/', views.new_release_paser),
    path('brand/', views.sneaker_data_by_brand_paser),
    path('test/', views.google_img_download),
    path('popular/', views.popular_release),
    path('img/pasing/', views.sneaker_img_paser),
    

] 