#Operaciones

'''
Se crean metodos que se van a llamar en otro archivo
'''

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error: Division por cero"
    return a/b