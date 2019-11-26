import numpy as np


def test_numpy_01(ejer_01):
    result = ejer_01()
    
    if not isinstance(result, np.ndarray):
        print("INCORRECTO - DEBE USARSE NUMPY ARRAY")
        return
    
    if list(result) == list(np.arange(0,11)):
        print("CORRECTO")
    else:
        print("INCORRECTO - {} es distinto de [0,1,2,3,4,5,6,7]".format( list(result)))

