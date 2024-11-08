"""
URL configuration for djangodb2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display_all_tables, name='display_all_tables'),
    path('add/user/', views.add_user, name='add_user'),
    path('add/car/', views.add_car, name='add_car'),
    path('add/service_station/', views.add_service_station, name='add_service_station'),
    path('add/service/', views.add_service, name='add_service'),
    path('add/order/', views.add_order, name='add_order'),
    path('delete/user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete/car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('delete/service_station/<int:station_id>/', views.delete_service_station, name='delete_service_station'),
    path('delete/service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('delete/order/<int:order_id>/', views.delete_order, name='delete_order'),
]
