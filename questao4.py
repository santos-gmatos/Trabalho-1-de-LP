import numpy as np

def interseccao(arr1, arr2):
    return np.intersect1d(arr1, arr2)

def indices_interseccao(arr1, arr2):
    A = np.where(np.isin(arr1, interseccao(arr1, arr2)))
    B = np.where(np.isin(arr2, interseccao(arr1, arr2)))
    return A, B
    

def diferenca(arr1, arr2):
    return np.setdiff1d(arr1, arr2)