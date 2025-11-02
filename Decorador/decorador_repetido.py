def repetir(n_veces):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n_veces):
                func(*args,**kwargs)
        return wrapper
    return decorador

@repetir(n_veces=3)
def decir_hola():
    print("Hola conchetumare")

decir_hola()