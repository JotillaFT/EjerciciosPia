import pandas as pd
import numpy as np

colnames = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv("iris.data", header=None, names=colnames)

valores_unicos = np.unique(df["class"])
print("Valores únicos da columna class:", valores_unicos)

mapa_clases = {clase: idx for idx, clase in enumerate(valores_unicos)}

df["class_numeric"] = df["class"].map(mapa_clases)
print("DataFrame con valores numéricos na columna 'class_numeric':")
print(df.head())

matriz_binaria = np.zeros((df.shape[0], len(valores_unicos)))

for idx, clase in enumerate(valores_unicos):
    matriz_binaria[:, idx] = (df["class"] == clase).astype(int)

for idx, clase in enumerate(valores_unicos):
    df[clase] = matriz_binaria[:, idx].astype(int)

print("DataFrame con columnas binarias para cada clase:")
print(df.head())
