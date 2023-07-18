# Ejercicio 1: filter
# Supongamos que tienes una lista de números y quieres filtrar solo los números pares. Puedes usar la función filter para hacerlo de la siguiente manera:

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda lista_numeros: lista_numeros % 2 == 0, numeros))
print(pares)