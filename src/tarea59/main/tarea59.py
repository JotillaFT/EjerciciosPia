import numpy as np

arr = np.arange(10)
print(arr)
arr2 = np.arange(1,11)
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pares = arr%2 == 0
impares = arr%2 != 0
arr[impares] =0
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.concatenate((a, b))
c2 = np.concatenate((a, b), axis=1)
print(arr)
print(arr2)
print(pares)
print(impares)
print(c)
print(c2)