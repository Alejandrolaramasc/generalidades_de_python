# %%
# Importar la base de datos athlete_events.csv , 
# y reportar la cantidad de registros (filas) y
#de campos (columnas). 
import pandas as pd
df = pd.read_csv('athlete_events.csv')
ejercicio_1 = df.shape
ejercicio_1
# %%
ejercicio_2 = df['Year'].value_counts().shape
ejercicio_2
# %%
ejercicio_3 = df['Season'].value_counts()/len(df["Season"])
ejercicio_3
# %%
query = df[df['Season'] == 'Summer']['Year'].min()
ejercicio_4a = query
ejercicio_4a
# %%
ejercicio_4b = df[df['Year'] == query]['City'].unique()
ejercicio_4b
# %%
query = df[df['Season'] == 'Winter']['Year'].min()
ejercicio_5a = query
ejercicio_5a
# %%
ejercicio_5b = df[df['Year'] == query]['City'].unique()
ejercicio_5b
# %%
ejercicio_6 = df['Team'].value_counts()[:10]
ejercicio_6
# %%
ejercicio_7 = df['Medal'].value_counts('%')
ejercicio_7
# %%
ejercicio_8 = df[df['Year'] == min(df['Year'])]['Team'].value_counts()
ejercicio_8

# %%
