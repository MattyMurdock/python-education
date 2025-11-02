'''
@staticmethod - Métodos que no necesitan acceso a la instancia (self) ni la clase (cls).
@classmethod - Métodos que reciben la clase como primer argumento (cls) en lugar de la instancia. 
'''

class MiClase:
    @staticmethod
    def metodo_estatico():
        print("No necesito ni self ni cls")

    @classmethod
    def metodo_de_clases(cls):
        print(f"Método de clase llamado desde {cls.__name__}")

MiClase.metodo_estatico() #No necesita instancia
MiClase.metodo_de_clases() #Recibe la clase automáticamente

