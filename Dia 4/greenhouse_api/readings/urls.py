from django.urls import path
from . import views

urlpatterns = [
    path('latest/<str:device_id>/', views.latest_reading),
    path('average/<str:device_id>/', views.average_reading),
]
