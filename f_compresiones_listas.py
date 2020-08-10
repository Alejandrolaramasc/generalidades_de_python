# %%
def divisible_por_5_o_3(n):
  return n % 3 == 0 or n % 5 == 0

lista = [1, 2, 15, 4, 256, 100, 60]
for result in map(divisible_por_5_o_3, lista):
    print(result)
#La función map le aplica una función a todos los elementos de una secuencia, 
# y retorna una secuencia con los retornos de la función aplicada.
# %%
lista = [1, 2, 15, 4, 256, 100, 60]
for result in map(lambda x: x % 3 == 0 or x % 5 == 0, lista):
    print(result)
#Lambda es una función anónima que se utiliza en compresiones de listas,
#patrón: lambda-argumentos-retorno

# %%
palabras = ["el", "animal", "come", "las", "América", "lo", "pos", "laguna"]
for palabra in filter(lambda x: len(x) > 3, palabras):
    print(palabra)
#La función filter, filtra una secuencia, en base a una función.


# %%
from functools import reduce
#reduce hay que importarla
lista = [1, 4, 9, 7, 10, 11]
print(reduce(lambda x, y: x + y, lista))
#La función reduce, es la forma funcional de agregar datos. 


# %%
cuadrados = list(map(lambda x: x**2, range(10)))
cuadrados

# %%
cuadrados = [x**2 for x in range(10)]
cuadrados
#si no se usa función lambda, la operación va al comienzo

# %%
alumnos = ['Ana', 'Luis', 'Pedro', 'Marta', 'Nerea', 'Pablo']
#lo siguiente entrega las iniciales de las mujeres de la lista
[alumno[0] for alumno in alumnos if alumno[-1] == 'a'] 
# %%
#lo siguiente entrega los nombres sólo de las mujeres de la lista
[alumno for alumno in alumnos if alumno[-1] == 'a']


# %%
#también podemos usar compresión de listas para diccionarios
notas = {'Ana':10, 'Luis':10, 'Pedro':4, 'Marta':7, 'Nerea':5, 'Pablo':6}
#con la siguiente condición podemos obtener los alumnos que aprobaron
[nombre for nombre, nota in notas.items() if nota >= 7]
#el método items() itera simultáneamente sobre claves y valores

