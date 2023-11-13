from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import time

current_time = time.strftime('%I:%M %p')
print(current_time)

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def procesar(request):
    try: 
        imagen_data = request.FILES['imagen'].read()
        imagen_array = np.frombuffer(imagen_data, np.uint8)
        imagen = cv2.imdecode(imagen_array, cv2.IMREAD_COLOR)

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Inicializar el clasificador de rostros
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detectar rostros en la imagen
        rostros = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(rostros) > 0:
            # Si se encontraron rostros, dibujar un rectángulo alrededor del primer rostro
            (x, y, w, h) = rostros[0]
            cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            mensaje = "Rostro encontrado"
        else:
            mensaje = "No se encontraron rostros"

        # Guardar la imagen con el rectángulo dibujado
        cv2.imwrite('static/imagen_procesada.jpg', imagen)

        return JsonResponse({'mensaje': mensaje})

    except Exception as e:
        return JsonResponse({'error': str(e)})
