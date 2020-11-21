

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login/',views.login, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('flights/',views.flights, name = 'flights'),
	path('picker/',views.picker, name = 'picker'),
    path('python/',views.python_example, name = 'python_example'),
	path('detail/',views.flight_detail_view, name = 'detail'),
    path('create/',views. create_flight_view, name = 'create_flight')
    ]


