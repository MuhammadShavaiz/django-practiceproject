from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello),
    path('about/', views.about, name='About'),
    path('youtube/', views.youtube, name='youtube'),
    path('analyze/', views.analyze, name='punctuation')
]

