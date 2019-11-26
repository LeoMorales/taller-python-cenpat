import numpy as np


def test_numpy_01(ejer_01):
    result = ejer_01()
    
    print("EJERCICIO 1:")
    if not isinstance(result, np.ndarray):
        print("\tINCORRECTO - DEBE USARSE NUMPY ARRAY")
        return 0
    
    if list(result) == list(np.arange(0,11)):
        print("\tCORRECTO")
        return 1
    else:
        print("\tINCORRECTO - {} es distinto de [0,1,2,3,4,5,6,7]".format( list(result)))
        return 0


def test_practica_02(funciones):
    puntaje = 0
    tests = [
        test_numpy_01
    ]
    for funcion_i, test_i in zip(funciones, tests):
        puntaje += test_i(funcion_i)
    
    print('\n\n{}\n\nEl puntaje obtenido es {} / {}\n\n{}'.format('#'*50, puntaje, len(tests), '#'*50))