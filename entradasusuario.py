# Pedir al usuario su nombre y edad
nombre = input("Por favor escriba su nombre, ¿Cuál es tu nombre?:")
edad = input("Por favor escriba su edad, ¿Cuántos años tienes?:")
# COnvertimos la edad a entero
edad = int(edad)
# Mostramos los resultados
print("Hola, ", nombre + " tienes ", edad, " años.")

# Ahora un ejercicio matematico
# pedir al usuario numeros
numero1 = float(input("Escribe un número: "))
numero2 = float(input("Escribe otro número: "))

# Realizamos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostramos los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

