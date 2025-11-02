'''
EStos son algunos de los decoradores más utlizados en Python:
@propety: Para definir getters y setters de atributos de una clase.
@functools.lru_cache: Para almacenar en caché los resultados de funciones costosas.
@app.route: En frameworks web como Flask, para definir rutas de URL.
'''

# Ejemplo con propety

class Circulo:
    '''
    Clase que representa un círculo con un radio.
    Parámetros:
        radio (float): El radio del círculo.
    Atributos:
        radio (float): El radio del círculo.
    Métodos:
        area: Calcula el área del círculo.
    '''
    def __init__(self, radio):
        '''
        Inicializa un objeto Circulo con el radio dado.
        Parámetros:
            radio (float): El radio del círculo. 
        '''
        self._radio = radio

    @property
    def radio(self):
        ''''
        Obtiene el valor del radio del círculo.
        Retorna:
            float: El valor del radio.
        '''
        return self._radio

    @radio.setter
    def radio(self, valor):
        '''
        Establece el valor del radio del círculo.
        Parámetros:
            valor (float): El nuevo valor del radio.
        Lanza:
            ValueError: Si el valor del radio es negativo.
        '''
        if valor < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

    @property
    def area(self):
        '''
        Calcula el área del círculo.
        𝑎 = π * r^2
        Donde r es el radio del círculo.
        Retorna:
        float: El área del círculo.
        '''
        import math
        return math.pi * (self._radio ** 2)


c = Circulo(5)
print("Radio:", c.radio)  # Accediendo al radio usando el getter
print("Área:", c.area)    # Calculando el área usando el método decorado con @property
c.radio = 10              # Estableciendo un nuevo valor para el radio usando el setter
print("Nuevo Radio:", c.radio)
print("Nueva Área:", c.area)