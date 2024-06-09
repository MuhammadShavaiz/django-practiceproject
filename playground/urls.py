from django.urls import path
from . import views

urlpatterns = [
    path('playground/', views.say_hello),
    path('about/', views.about, name='About'),
    path('youtube/', views.youtube, name='youtube')
]

