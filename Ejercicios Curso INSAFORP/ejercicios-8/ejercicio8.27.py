def par_impar(entero):
    if entero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado

entero = int(input("ingresar un numero entero para verificar: "))
print(f"el numero {entero} es {par_impar(entero)}")