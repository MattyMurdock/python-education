#! Usando If
#* escribir un programa donde el usuario ingrese dos numeros y luego se determine cual de los dos es mayor o si son iguales

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

# hacemos la parte donde se checa cual es mayor o sis on iguales

if num1 > num2:
    print("El primer numero es mayor que el segundo")
elif num1 < num2:
    print("El segundo numero es mayor que el primero")
else:
    print("Los numeros son iguales")

#* NOTA: en python no se pueden hacer comparaciones 
# entre numeros y strings, por lo que 
# si se intenta hacer una comparacion entre un numero y un string, 
# python arrojara un error
#typeError: '>' not supported between instances of 'str' and 'int'

#! Ejecutando un for
# se usa para iterar sobre una secuencia, como una lista, tupla, diccionario
# o conjunto o cadena
#? Es ideal cuando sabes cuantas veces se debe repetir una tarea o cuando quieres
#? iterar sobre una coleccion de elementos.

#* Ejemplo de un for
for i in range(1,11): #genera numeros del 1 al 10
    print(i)

#! Ejecutando un while
# es util cuando no se sabe cuantas veces se debe repetir una tarea
# pero se tiene una condicion que se debe de cumplir para que el ciclo se ejecute

#? Ejemplo
numero_secreto = 7

#iniciamos una variable para almacenar la supocision del usuario
suposicion = None

# BUcle while para pedir al usuario adivine
while suposicion != numero_secreto:
    suposicion = int(input("Adivina el numero secreto entre 1 y 10: "))

    if suposicion == numero_secreto:
        print("Felicidades, adivinaste el numero secreto es: " + str(numero_secreto))
    else:
        print("Numero incorrecto, intenta de nuevo amiko :3/")

# Escribe un programa que imprima los números del 1 al 20, pero para los múltiplos de 3 imprima "Fizz", para los múltiplos de 5 imprima "Buzz", y para los múltiplos de ambos 3 y 5 imprima "FizzBuzz"

for i in range(1, 21): # lista del 1 al 20
    if i % 3 == 0 and i % 5 == 0: # si el numero es multiplo de 3 y 5
        print("FizzBuzz") # imprime FizzBuzz 
    elif i % 3 == 0: #si el numero es multiplo de 3
        print("Fizz") # imprime Fizz
    elif i % 5 == 0: # si el numero es multiplo de 5
        print("Buzz") # imprime Buzz
    else:
        print(i) # imprime el numero
