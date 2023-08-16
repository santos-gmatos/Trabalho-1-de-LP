import numpy as np

def empilhamento_horizontal(arr1, arr2):
    return np.vstack((arr1, arr2))
    
    
def dados_estatisticos(arr):
    print(np.average(arr))
    print(np.std(arr))
    print(np.var(arr))
    
    
def par_impar(arr):
    