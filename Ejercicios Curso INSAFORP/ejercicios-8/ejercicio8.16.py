def es_primo(numero): #funcion para definir si es numero primo
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1): # numero ** 0.5 es para ver raiz cuadrada, +1 para iterar mas
        if numero % i == 0:
            return False
    return True

cantidad_primos = 0

while True:
    numero = int(input("Ingresa un número mayor que 1 (ingresa 0 para terminar): "))
    
    if numero == 0:
        break
    elif es_primo(numero):
        cantidad_primos += 1
        print(f"{numero} es primo")
    else:
        print((f"{numero} no es primo"))

print(f"Cantidad de números primos ingresados: {cantidad_primos}")
