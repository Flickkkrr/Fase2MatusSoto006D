from django.urls import path #Importar URLS
from . import views #Importar vistas

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tienda/', views.proximamente, name ='proximamente'),
    path('autocultivo/', views.autocultivo, name='autocultivo'),
    path('quienes/', views.quienes, name='quienes'),
    path('registro/', views.registro, name='registro'),
]

