
import pandas as pd
dict = {
"country":["Brazil", "Russia", "India", "China", "South Africa"],
"capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
"area":[8516, 17100, 3286, 9597, 1221],
"population":[200.4, 143.5, 1252, 1357, 52.98] }
paises = pd.DataFrame(dict)
print(paises)




