from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('produk/', views.daftar_produk, name='daftar_produk'),
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),
    path('kontak/', views.kontak, name='kontak'),
     path('about/', views.about, name='about'),
    
]