from django.urls import path
from . import views

urlpatterns = [
        path('', views.hello),
        path('listar_sensores/', views.listar_sensores),
        path('sensores/', views.sensor_list_create),
]