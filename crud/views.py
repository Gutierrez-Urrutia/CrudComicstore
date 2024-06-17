from django.shortcuts import render
from .models import Comic

# Create your views here.
def agregar(request):
    return render(request, 'crud/agregar.html') 

def actualizar(request):
    return render(request, 'crud/actualizar.html')  

def crud(request):
    context ={}
    return render(request, 'crud/crud.html', context)

def eliminar(request):
    return render(request, 'crud/eliminar.html')

def listar(request):
    comics = Comic.objects.all()
    return render(request, 'crud/listar.html', comics)



