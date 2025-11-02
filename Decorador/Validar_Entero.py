# Este decorador valida que el argumento pasado a la función sea un entero positivo.
def validar_entero(func):
    def wrapper(n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("El argumento debe ser un entero.")
        return func(n)
    return wrapper

# Ejemplo de uso del decorador: Aqui se usa el decorador para validar el argumento de la función factorial.
@validar_entero
def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)

try: 
    print(factorial(5))  # Salida: 120
    print(factorial(-3)) # Esto lanzará una excepción
except ValueError as e:
    print(f"Erro:{e}") # Salida: El argumento debe ser un entero.