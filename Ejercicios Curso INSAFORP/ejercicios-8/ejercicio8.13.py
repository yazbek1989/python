lista = []
while True:
    positivo = int(input("ingrese numeros positivos o '0' para salir: "))
    if positivo == 0:
        break
    elif positivo > 0:
        lista.append(positivo)
    else:
        print("ingresar un numero positivo")
        
print(f"el numero mayor es: {max(lista)} de {lista}")
        