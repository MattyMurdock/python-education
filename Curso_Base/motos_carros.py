# vamos a hacer un sistema de vehiculos que aceleren de forma distinta

# Definir clase
class Vehiculo:
    def acelerar(self):
        raise NotImplementedError("Este método debe ser implementado")

class Coche(Vehiculo):
    def acelerar(self):
        return "El coche acelera pisando el acelerador"
class Moto(Vehiculo):
    def acelerar(self):
        return "La moto acelera girando el puño del acelerador"
class Bicicleta(Vehiculo):
    def acelerar(self):
        return "La bicicleta acelera pedaleando"

# Demostración polimorfismo
def probar_aceleracion(vehiculo):
    print(vehiculo.acelerar())
# Crear instancias de coches y moto
mi_coche = Coche()
mi_moto = Moto()
# Mismos metodos, comprtamientos deferentes
probar_aceleracion(mi_coche)  # Salida: El coche acelera pisando el acelerador
probar_aceleracion(mi_moto)  # Salida: La moto acelera girando el puño del acelerador

# Aprendimos que:
'''
Polimorfismo en acción: Ambos objetos responden al método acelerar(), pero cada uno lo hace a su manera.
Ventaja clave: Podemos agregar nuevos vehículos (bicicletas, camiones) sin modificar la función probar_aceleracion.
'''
# Implementar metodo de bicicleta
mi_bici = Bicicleta()
probar_aceleracion(mi_bici)  # Salida: La bicicleta acelera pedaleando
