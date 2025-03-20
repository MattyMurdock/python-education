'''
Trabajar con archivos en Python
1. Nombre del archivo o ruta que se desea abrir
2. Modo en que se desea abrir el archivo
    - r: lectura
    - w: escritura (si el archivo no existe, se crea)
    - a: escritura (añadir al final del archivo)
    - x: escritura (si el archivo no existe, si no, error)
    - b: binario (para archivos no de texto)
    - t: texto (por defecto)
'''

# Abrir un archivo en modo lectura
with open('test/datos.txt', 'r') as archivo:
    contenido = archivo.read()
#imprimir
print(contenido)

# Escribir en un archivo
# Abrir archivo en modo escritura
with open('test/notas.txt', 'w') as archivo:
    archivo.write('Nota 1: Dónde estamos? \n')
    archivo.write('Nota:2 Abgar un rey de Odesa\n')
    archivo.write('Nota 3: La historia de la humanidad\n')
#imprimir msg
print("Se ha escrito en el archivo 'notas.txt'")

# Leer y procesar un archivo
suma = 0
with open('test/nums.txt', 'r') as archivo:
    for linea in archivo:
        suma += int(linea.strip()) #strip() elimina los espacios en blanco
# escribir el resultado
with open('test/suma_resultado.txt', 'w') as archivo:
    archivo.write(f'La suma de los números es: {suma}')
print("Se ha escrito en el archivo 'suma_resultado.txt'")

# Modificar un archivo
# Se crea un archivo de frutas.txt
with open('test/frutas.txt', 'a') as archivo:
    archivo.write('\nUva')
    archivo.write('\nMango')
    archivo.write('\nPiña')
# leer y mostrar el contenido
with open('test/frutas.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)