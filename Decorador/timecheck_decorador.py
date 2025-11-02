'''
Crear un decorador que mida el tiempo de ejecución de una función.
'''
import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

# usamos el decorador
@medir_tiempo
def calcular_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
# llamamos la funcion
print(calcular_factorial(1000)) #se mide el tiempo de ejecución automaticamente