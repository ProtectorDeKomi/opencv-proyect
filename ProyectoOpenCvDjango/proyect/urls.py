# tu_proyecto/urls.py
from django.urls import path
from openCv.views import index, procesar  # Asegúrate de que la importación sea correcta

urlpatterns = [
    path('', index, name='index'),
    path('procesar', procesar),
]
