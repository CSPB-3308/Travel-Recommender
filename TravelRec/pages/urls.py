from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('recommendations/', views.recommendation_view, name='recommendations'),
]