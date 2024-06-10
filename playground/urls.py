from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello),
    path('about/', views.about, name='About'),
    path('contact/', views.contact_me, name='contact'),
    path('analyze/', views.analyze, name='punctuation')
]

