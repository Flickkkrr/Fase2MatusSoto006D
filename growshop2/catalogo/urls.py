from django.urls import path #Importar URLS
from . import views #Importar vistas

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tienda/', views.proximamente, name ='proximamente'),
    path('autocultivo/', views.autocultivo, name='autocultivo'),
    path('quienes/', views.quienes, name='quienes'),
    path('registro/', views.registro, name='registro'),
    path('cepa1/', views.cepa1, name='cepa1'),
    path('seta1/', views.seta1, name='seta1'),
    path('terminosycon/', views.terminosycon, name='terminosycon')
]
