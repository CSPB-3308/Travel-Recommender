

from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name = 'index'),
	path('picker/',views.picker, name = 'picker'),
	path('detail/',views.flight_detail_view, name = 'detail'),
        ]

