# %%
#DataFrame desde diccionario en la consola
dict = {
"country":["Brazil", "Russia", "India", "China", "South Africa"],
"capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
"area":[8516, 17100, 3286, 9597, 1221],
"population":[200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd
paises = pd.DataFrame(dict)
print(paises)
# %%
#para guardar un dataframe como archivo csv
paises.to_csv('countries.csv')

# %%
# analisis exploratorio
type(paises)
# %%
paises.shape
# %%
paises.columns 
# %%
paises.info()
# %%
paises.head(3)
# %%
paises.describe()
# %%
#loc es un método pandas para DF análogo a brackets en lsitas
#para seleccionar 1 fila:
paises.loc[[1]]

# %%
#para seleccionar varias filas:
paises.loc[[0, 2, 4]]

# %%
#para seleccionar filas y columnas:
paises.loc[[1, 3], ["area", "population"]]

# %%
print(paises[1:4])
# %%
#si pones la componente “x” como 2 puntos obtienes todas las filas
paises.loc[:,["country", "capital"]]

# %%
#iloc es otro método pandas que sólo filtra por índices
#para seleccionar filas y columnas:
paises.iloc[[1, 3], [0, 1, 2]]
#a diferencia de los brakets en listas, iloc incluye 
#el último valor
# %%
#y si pones : en la coordenada “y” te va a mostrar todas las columnas
paises.iloc[[0, 1],:]

# %%
#para filtar por más de una condición y para hacer
#calculos matemáticos con el dataframe debemos importar numpy
import numpy as np 
paises[np.logical_and(paises["area"] > 8000, paises["area"] < 10000)][["country"]]

# %%
#agregar una nueva columna, por ejemplo, a partir de un calculo:
for lab, row in paises.iterrows():
    paises.loc[lab, "name_length"] = len(row["country"])
print(paises)

