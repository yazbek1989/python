
# creando una lista con list
lista = list(["hola","dalto",34,40,50,60])

# devuelve la cantida de elementos de la lista
cantidad_elementos = len(lista)

# agregando un elemento a la lista
lista.append("JAJJAJAJAJ")

# agregando un elemento a la lista en un indice especifico
lista.insert(2,"TOMA MAMA")

# agregando varios elementos a la lista (tiene que ser una lista con la que se use)
lista.extend(["uno",3023,"trusted"])

# eliminando un elemento de la lista, tiene que pasarse con el indice
# para eliminar el ultimo elemento de la lista o el penultimo es -1 y -2 los negativos en reversa del ultimo hacia el primero
lista.pop(-1)

# removiendo un elemento de la lista por su valor, lanza excepcion si no encuentra el parametro
lista.remove("TOMA MAMA")

# sort es para ordenar de forma ascendente, solo funciona cuando no hay cadenas de texto
# tira excepcion si hay alfabeticos, buleanos (false primero y true despues antes que los numeros)
# lista.sort(reverse=true) ordena y despues revierte los elementos de la lista
# lista.sort()

# invierte todos los parametros que hay en la lista
lista.reverse()

# clear elimina todo los elementos de la lista
# lista.clear()

# verificando si un elemento se encuentra en la lista, verifica elementos completos no verifica lo que contiene cada elemento
# esto mismo se aplica a las tuplas
elemento_encontrado = lista.index('uno')


print(elemento_encontrado)