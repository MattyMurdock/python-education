'''
Una funcion se define con def seguida del nombre y su parentesis ()
Contienen parametros que son los valores que se le pasan a la funcion si los hay
El cóodigo de la funcion se escribe con sangria
Para retornar un valor se usa la palabra reservada return
'''

def saludar(nombre):
    return f"hola, {nombre}, ¿como estas?"
#hay que llamar la funcion para que se ejecute
msg = saludar("Arcoterios")
print(msg)

# Ejemplo de funcion con varios parametros
def suma(a, b):
    return a + b
#llamamos a la funcion y guardamos el resultado en una variable
resultado = suma(10, 20)
print("La suma es: ", resultado)

# Funcion con un valor predeterminado
def calcular_area(base, altura=None):
    if altura is None:
        altura = base #si no se pasa la altura se toma como cuadrado
    #es un cuadrado
    return base * altura
#llamamos a la funcion y guardamos el resultado en una variable
area_rectangulo = calcular_area(10, 20)
area_cuadrado = calcular_area(10)
#imprimimos los resultados
print("El area del rectangulo es: ", area_rectangulo)
print("El area del cuadrado es: ", area_cuadrado)

# Ejercicio: Escribe una función llamada es_primo que tome un número como parámetro y devuelva True si el número es primo, y False si no lo es. Luego, usa esta función para imprimir todos los números primos entre 1 y 50.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# imprimir los numeros primos entre 1 y 50
for i in range(1, 51):
    if es_primo(i):
        print(i, end=' ')
print()

## Otra forma de hacerlo
def es_primo_v2(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Imprimir todos los números primos entre 1 y 50
print("Números primos entre 1 y 50 con la segunda version:")
for num in range(1, 51):
    if es_primo_v2(num):
        print(num, end=" ")