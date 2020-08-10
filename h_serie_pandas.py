# %%
# Hay pequeñas diferencias entre una serie pandas y 
#un DataFrame de 1 sola columna, el DF tiene nombre
#de la columna, la serie no (header) y un grupo chico
#de funciones son propias de cada uno.
import pandas as pd
pd.Series([True, False, True])

# %%
pd.Series([True, False, True]) & pd.Series([False, True, True])

# %%
pd.Series([True, False, True]) | pd.Series([False, False, True])

# %%
