# Crear una lista de frutas
frutas = ["manzana", "plátano", "naranja", "uva", "Mango"]

# Imprimir la lista completa
print("Lista de frutas:", frutas)

# Imprimir el primer elemento de la lista
print("Mi fruta favorita es:", frutas[4])

# Se pueden agregar elementos append()
# eliminar elelemntos remove() o todo con pop()
# tomar la longitud con len()
# Iterar con for
# ordenar con sort()
# invertir con reverse()
# buscar con index()
# contar con count()
# insertar con insert()
# extender con extend()
# copiar con copy()
# limpiar con clear()

# Ejercicio de práctica
#* crear lista de numeros
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#* Agregar un numero nuevo
numeros.append(110)
#* Eliminar el primer elemento de la lista
numeros.pop(0)
#* Imprimir la longitud de la lista
print("Longitud de la lista:", len(numeros))
#* Recorrer la lista e imprimir cada elemento
print("Recorriendo la lista:")
for numero in numeros:
    print(numero)

# Ejercicio avanzado con listas
#* lista vacia
nums = []
#* Pedir un numero al usuario 5 veces
for i in range(5):
    num = float(input(f"Ingresa un número {i +1} : "))
    nums.append(num)
#* calcular la suma, el maximo y el minimo
suma = sum(nums)
maximo = max(nums)
minimo = min(nums)
#* Imprimir los resultados
print("lista de numeros:", nums)
print("La suma es:", suma)
print("Numero maximo:", maximo)
print("Numero minimo:", minimo)