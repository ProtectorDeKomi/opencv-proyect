# models.py
import hashlib
import os

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    datos_biometricos_hashed = models.TextField()
    datos_biometricos_salt = models.CharField(max_length=50)
    imagen_rostro = models.ImageField(upload_to='rostros/')

    def __str__(self):
        return self.nombre

    def set_datos_biometricos(self, datos_biometricos):
        # Generar un salt único para cada usuario
        salt = os.urandom(32)
        # Concatenar los datos biométricos con el salt y luego hashearlos
        hashed_datos_biometricos = hashlib.pbkdf2_hmac('sha256', datos_biometricos.encode('utf-8'), salt, 100000)
        self.datos_biometricos_hashed = hashed_datos_biometricos
        self.datos_biometricos_salt = salt.hex()

    def verificar_datos_biometricos(self, datos_biometricos):
        # Recuperar el salt almacenado y hashear los nuevos datos biométricos
        salt = bytes.fromhex(self.datos_biometricos_salt)
        hashed_datos_biometricos = hashlib.pbkdf2_hmac('sha256', datos_biometricos.encode('utf-8'), salt, 100000)
        # Verificar si los datos biométricos hasheados coinciden con los almacenados
        return hashed_datos_biometricos == self.datos_biometricos_hashed
