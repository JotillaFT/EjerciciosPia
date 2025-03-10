import numpy as np
import pandas as pd

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = a==b
d = a[c]
a2 = np.array([2, 6, 1, 9, 10, 3, 27])
print(a2)
filtroa = np.where((a2>=5) & (a2<= 10))
print(c)
print(d)
print(a2[filtroa])

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y
    
pair_max = np.frompyfunc(maxx, 2, 1)

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(pair_max(a, b))

columnas = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']
data = pd.read_csv('iris.data', header=None, names=columnas)

sepallength = data['sepallength'].to_numpy()

min_val = sepallength.min()
max_val = sepallength.max()

sepallength_normalized = (sepallength - min_val) / (max_val - min_val)

print("Sepallength normalizado:")
print(sepallength_normalized)