import numpy as np
import numpy.random as npr
import questao1 as q1
import questao2 as q2
import questao3 as q3
import questao4 as q4
import questao5 as q5
#import questao6 as q6
#import questao7 as q7


# question 1
print("-="*50)

arr1 = np.arange(10) # array1
arr2 = np.ones(10) # array2

arr3 = q1.soma(arr1, arr2)
   
print(f"O primeiro array é:     {arr1}\n")
print(f"O segundo array é:      {arr2}\n")
print(f"O terceiro array é:     {arr3}\n")
    

# question 2
print("-="*50)

arr3 = q2.redimensiona(arr3) # array3 with 2 lines

print(f"O terceiro array com 2 dimensões agora é:\n{arr3}\n")

arr3 = q2.converte_para_float(arr3) # numbers to float numbers

print(f"O terceiro array com pontos flutuantes agora é:\n{arr3}\n")

arr3 = q2.transposta(arr3) # transposta do array3

print(f"A transposta do array 3 é:\n{arr3}\n")


# question 3
print("-="*50)

arr4 = np.linspace(1, 10, 10).reshape((5, 2)) # array4

print(f"O quarto array é:\n{arr4}\n")

arr4 = q3.multiplica(arr4, arr3) # array4 x array3

print(f"O quarto, após a multiplicação pelo terceiro, array agora é:\n{arr4}\n")


# question 4
print("-="*50)

arr5 = npr.randint(1, 100, 50) # array5
arr6 = npr.randint(1, 100, 50) # array6
arr56 = q4.interseccao(arr5, arr6) #intersecção array5 e array6
ind_arr5, ind_arr6 = q4.indices_interseccao(arr5, arr6) # indices dos elementos comuns em array5 e array6
arr5_6 = q4.diferenca(arr5, arr6)
print(f"O quinto array é:       {arr5}\n")
print(f"O sexto array é:        {arr6}\n")
print(f"Os elementos de comuns a ambos os arrays (quinto e sexto) são:            {arr56}")
print(f"Os índices dos elementos da intersecção que estão no quinto array são:    {ind_arr5}")
print(f"Os índices dos elementos da intersecção que estão no sexto array são:     {ind_arr6}")
print(f"Os elementos do quinto array que não estão no sexto são:                  {arr5_6}")


# question 5
print("-="*50)

arr7 = q5.empilhamento_horizontal(arr5, arr6)

print(f"O sétimo array é: {arr7}")

q5.dados_estatisticos(arr7)

# question 6
print("-="*50)


# question 7
print("-="*50)
