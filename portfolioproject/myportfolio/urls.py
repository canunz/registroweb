from django.urls import path
from .views import index, evento, registro

urlpatterns = [
    path('', index, name='home'),  # Asegúrate de que este es el patrón para la vista index
    path('evento/', evento, name='evento'),
    path('registro/<str:nombre_evento>/<str:tipo_evento>/', registro, name='registro'),
]
