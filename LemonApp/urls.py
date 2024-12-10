from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('menu/', views.menu, name='menu'),  # Menu page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('order/', views.order, name='order'),
    path('confirm/',views.confirm, name='confirm'),
]
