'''
Modulos son archivos que contienn codigo python, funciones, clases variables
que pueden ser importados en otros archivos python
Algunos ya vienen por defecto en python pero se pueden crear propios
'''
import math
import random

# Para sacar la raiz cuadrada de un numero
numero = 25
raiz_cuadrada = math.sqrt(numero)
print(f"La raiz cuadrada de {numero} es {raiz_cuadrada}")

# hacer un numero aleatorio
num_random = random.randint(1, 100)
#Iniciar la variable para almacenar la supocicion del usuario
suposicion = None
# Iniciar el contador de intentos
while suposicion != num_random:
    suposicion = int(input("Adivina el numero (entre 1 y 100): "))
    if suposicion > num_random:
        print("Muy alto")
    elif suposicion < num_random:
        print("Muy bajo")
    else:
        print("COrrecto! Adivinaste el numero")
        break
