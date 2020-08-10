# %%
#List slicing
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam
# %%
fam[3:5]
#excluye el último valor límite
# %%
fam[:4]
#parte desde posición 0 hasta posición 3.
# %%
fam[5:]
#parte en la posición 5 hasta la posición final.

# %%
#Changing list elements
fam
['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]
# %%
fam[0:2] = ["lisa", 1.74]
fam
#cambia valores 0 y 1 por los señalados

# %%
#Adding and removing elements
fam_ext = fam + ["me", 1.79]
fam_ext
# Si queremos guardar la nueva lista.

# %%
del(fam[2])
fam
#borra la posición 2

# %%
#Al usar zip() con n argumentos, entonces la función devolverá un iterador
#que genera tuplas de longitud n. Se usa para hacer listas anidadas.
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)
z_list = list(z)
print(z_list)

# %%
#Functions
#Examples simple
fam1 = [1.73, 1.68, 1.71, 1.89]
max(fam1)

# %%
round(1.68, 1)

# %%
round(1.68)

# %%
type(fam)

# %%
#uso método replace a un string
sister = "liz"
sister.replace("z", "sa")
#la segunda posición es el elemento que entra

# %%
#uso método append a una lista
fam.append("me")
fam
# %%
fam.append(1.79)
fam