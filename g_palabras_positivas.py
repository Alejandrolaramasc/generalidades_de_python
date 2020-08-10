# NLP - Natural Language Processing with Python es un área
#del machine learning que ocupa mucho análisis de textos
PALABRAS_POSITIVAS = {
  "beneficios",
  "excelentes",
  "buen",
  "positivo",
  "optimista",
  "encanta",
  "bien",
}

oraciones = [
    "El producto es un asco",
    "Los beneficios son excelentes",
    "En el restorán tuve un muy buen servicio",
    "Soy muy positivo y optimista y me encanta hablar bien de los demás",
]

conteo = map(lambda s: sum(s.count(w) for w in PALABRAS_POSITIVAS), oraciones)
for index, conteo in enumerate(conteo):
    print(f"Palabras positivas oración {index + 1}: {conteo}")
#Lo que da como salida:

#Palabras positivas oración 1: 0
#Palabras positivas oración 2: 2
#Palabras positivas oración 3: 1
#Palabras positivas oración 4: 4