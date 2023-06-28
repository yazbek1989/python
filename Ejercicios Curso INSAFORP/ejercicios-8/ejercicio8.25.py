def contar_nombre(nombre):
    contar = 0
    for i in nombre:
        contar += 1
    return contar

nombre = input("ingrese su nombre: ")
print(f"{nombre} tiene {contar_nombre(nombre)} letras")
