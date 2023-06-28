# creando un conjunto con funcion set
conjunto = set(["dato1", "dato2","dato3",1,2,3,4,5])

# metiendo un conjuntoi dentro de otro conjunto
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato 3"}

# enumerate me permite iterar conjuntos en pares de datos (hace como un indice artificial porque los conjuntos no tienen indice)
for con in enumerate(conjunto):
    print(f"iterar conjunto {con[1]}")

print(type(conjunto2))
print(conjunto2)

# teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

print(resultado)

# superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1

print(resultado)

# verificar si hay algun numero en comun. solo da true cuando no hay ni un solo numero que sea igual en los conjuntos
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)