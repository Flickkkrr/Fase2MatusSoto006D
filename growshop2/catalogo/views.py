from django.shortcuts import render
from . models import Categoria, Accesorio, InstanciaAccesorio, Marca
from django.views import generic

# Create your views here.
def inicio(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'inicio.html',
        context={'num_catego':num_catego},
    )

def proximamente(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'proximamente.html',
        context={'num_catego':num_catego},
    )

def autocultivo(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'autocultivo.html',
        context={'num_catego':num_catego},
    )

def quienes(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'quienes.html',
        context={'num_catego':num_catego},
    )

def registro(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'registro.html',
        context={'num_catego':num_catego},
    )

