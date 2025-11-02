''' Diccionarios EN Python
Un diccionario se define usando llaves {} y los pares clave-valor se separan con comas.
Cada par clave-valor tiene la forma clave: valor.
Las claves deben ser únicas y pueden ser de cualquier tipo inmutable (como cadenas, números o tuplas).
Los valores pueden ser de cualquier tipo (números, cadenas, listas, otros diccionarios, etc.).'
'''
#* Diccionario con info persona
persona = {
    "nombre": "Arcoterios",
    "apellido": "Von Bismark",
    "edad": 25,
    "ciudad": "Tuxtla"
}
#*¨Imprimir el diccionario completo
print("Diccionario completo:", persona)
#* Imprimir el nombre de la persona
print("Nombre:", persona["nombre"])

''' Operaciones comunes con diccionarios
Agregar un nuevo par clave-valor: Simplemente asigna un valor a una nueva clave.
Modificar un valor: Asigna un nuevo valor a una clave existente.
Eliminar un par clave-valor: Usa del o pop().
Verificar si una clave existe: Usa in.
Recorrer un diccionario: Usa un bucle for para iterar sobre las claves, valores o ambos.
'''

#* Crear un dicionario con edades de personas
edades = {
    "Arcoterios": 25,
    "Fernando": 30,
    "Luis": 35
}

#* Agregar una nueva persona
edades["Carlos"] = 40
#* Modificar la edad de Arcoterios
edades["Arcoterios"] = 26
#* Eliminar
del edades["Fernando"]
#? Verificar si existe Arcoterios
if "Arcoterios" in edades:
    print("Arcoterios tiene", edades["Arcoterios"], "años")
#* Imprimir la info
print("Edades actualizadas:", edades)

#! Ejerccio avanzado con diccionarios
#* crear un diccionario vacio
old_year = {}
#* pedir al usuario que ingrese la edad de 3 personas
for i in range(3):
    nombre = input(f"Ingresa el nombre de la persona {i + 1}: ")
    edad = int(input(f"Ingresa la edad de la persona {i + 1}: "))
    old_year[nombre] = edad
#* Imprimir el diccionario
print("Diccionario de edades:", old_year)
#* encontrar la persona mas joven
persona_joven = min(old_year, key=old_year.get)
edades_mas_joven = old_year[persona_joven]
#* Imprimir los resultados
print(f"La persona más joven es {persona_joven} con {edades_mas_joven} años")