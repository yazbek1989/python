def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        bit = int(binario[i])
        exponente = longitud - i - 1
        decimal += bit * (2 ** exponente)
    return decimal

def decimal_a_binario(decimal):
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

seleccion = input("opcion 1: convertir de binario a decimal\nopcion 2: convertir de decimal a binario: ('1'/'2'): ")
if seleccion == "1":
    binario = input("Ingrese el numero binario: ")
    print(f"el numero decimal es: {binario_a_decimal(binario)} ")
if seleccion == "2":
    decimal = int(input("Ingrese el numero decimal: "))
    print(f"el numero binario es: {decimal_a_binario(decimal)} ")