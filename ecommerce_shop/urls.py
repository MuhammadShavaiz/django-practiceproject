from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name = 'contact'),
    path('tracker/',views.tracker, name = 'tracker'),
    path('productView/',views.productView, name = 'productView'),
    path('search/',views.search, name = 'search'),
    path('checkout/',views.checkout, name = 'checkout'),
]
