'''
Un decorador es una función que recibe otra función como argumento y devuelve una nueva función que generalmente extiende el comportamiento de la función original.
Es como "envolver" una función con otra función.
'''

def default_decorator(func):
    def wrapper():
        print("Algo ocurre ANTES de llamar a la función")
        func()
        print("Algo ocurre DESPUES de llamar a la función")
    return wrapper
#decorador en funcionamiento
@default_decorator
def saludar():
    print("Hola, ¿cómo estás?")
# llamamos la funcion
saludar()
