# Ejercicio 3: reduce
# Si deseas calcular la suma de todos los elementos en una lista, puedes utilizar la función reduce de la biblioteca functools:
from functools import reduce

numeros = [33,31, 68]
print(reduce(lambda a, b : a + b, numeros))