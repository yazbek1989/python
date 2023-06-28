lista = []
while True:
    insert = float(input("insertar un numero o '0' para salir: "))
    if insert == 0:
        break
    else:
        lista.append(insert)
      
lista.sort(reverse=True)
print(lista)
