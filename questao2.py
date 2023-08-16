import numpy as np

def redimensiona(arr):
    size = len(arr)
    ncol = int(size / 2)
    
    return arr.reshape((2, ncol))


def converte_para_float(arr):
    return arr.astype(np.float64)


def transposta(arr):
    return arr.transpose()