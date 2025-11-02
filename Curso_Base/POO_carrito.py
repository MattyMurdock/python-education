# Definir clase de coche
class Coche:
    def __init__(self, marca, modelo, color, precio, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.__año = año  # Atributo privado

    def obtener_año(self):
        return self.__año

    def descripcion(self):
        return f"Coche {self.marca} {self.modelo} de color {self.color} con precio {self.precio}"

# Crear objeto
mi_carrito = Coche("Ford", "Fiesta", "Blanco", 150000, 2025)

# Llamar al método descripcion
print("Descripción del coche:", mi_carrito.descripcion())

# Clase con herencia
class CocheElectrico(Coche):
    def __init__(self, marca, modelo, color, precio, autonomia, año):
        super().__init__(marca, modelo, color, precio, año)  # Llamar al constructor de la clase padre
        if autonomia <= 0:
            raise ValueError("La autonomía debe ser mayor a 0")
        self.autonomia = autonomia

    def mostrar_info(self):
        return f"Coche {self.marca} {self.modelo} de color {self.color} con precio {self.precio} y autonomía {self.autonomia} km"

# Intentar crear un objeto con autonomía negativa
try:
    mi_coche_electrico = CocheElectrico("Tesla", "Model S", "Rojo", 1000000, -100, 2012)
except ValueError as e:
    print("Error:", e)

# Crear objeto correctamente
mi_coche_electrico = CocheElectrico("Tesla", "Model S", "Rojo", 1000000, 500, 2012)

# Llamar métodos
print("Descripción del coche eléctrico:", mi_coche_electrico.mostrar_info())

# Agregar año al coche
mi_carrito = Coche("Ford", "Fiesta", "Blanco", 150000, 2021)
print("Año del coche:", mi_carrito.obtener_año())