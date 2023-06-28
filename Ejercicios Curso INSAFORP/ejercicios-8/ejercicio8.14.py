numero = int(input("Ingrese un número entero positivo: "))
suma = 0

while numero > 0:
    digito = numero % 10  # Obtiene el último dígito (% da como resultado el residuo)
    suma += digito  # Suma el dígito al total
    numero //= 10  # Elimina el último dígito (// da el resultado eliminando el residuo)

print(f"La suma de los dígitos es: {suma}")