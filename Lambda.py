import time, functools 

def calculateTime(funcion):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = funcion(*args, **kwargs)
        end_time = time.time()
        print(f'la ejecucion de la función tardo {end_time - start_time}')
        return result
    return wrapper

def makeUpper_decorador(funcion):
    def wrapper():
        result = funcion()
        makeUppercase = result.upper()
        return makeUppercase
    return wrapper



def makeList(funcion):

        @functools.wraps(funcion)
        def wrapper():
            func = funcion()
            splitted_string = func.split()
            return splitted_string
        return wrapper


@calculateTime
def suma(a, b):
    time.sleep(2)  # Simulando una operación larga en tiempo de ejecución
    return a + b

@calculateTime
def multiplicacion(a, b):
    time.sleep(1)  # Simulando una operación larga en tiempo de ejecución
    return a * b

@makeList
@makeUpper_decorador
def convertir_a_mayusculas():
    return 'hola mundo!'


print(suma(3, 5))


print(multiplicacion(4, 7))

print(convertir_a_mayusculas())