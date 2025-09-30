from django.urls import path
from . import views

urlpatterns = [
        path('',views.hello),
        path('about/', views.about),
        path('sensores/', views.mostrar_sensores),
        path('sensor/<int:sensor_id>/', views.mostrar_sensor),
        path('api/sensores/', views.listar_sensores),
]