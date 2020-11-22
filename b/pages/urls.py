from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('recommendations/', views.recommendation_view, name='recommendations'),
    path('recommendations/lodging/', views.lodging_view, name='lodging'),
    path('recommendations/attractions/', views.attractions_view, name='attractions'),
    path('recommendations/restaurants/', views.restaurants_view, name='restaurants'),
]