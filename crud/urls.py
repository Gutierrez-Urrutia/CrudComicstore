from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name='crud'),
    path('agregar/', views.agregar, name='agregar'),
    path('actualizar/<int:id>/', views.actualizar, name='actualizar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('listar/', views.listar, name='listar'),

    # Add more paths here
]