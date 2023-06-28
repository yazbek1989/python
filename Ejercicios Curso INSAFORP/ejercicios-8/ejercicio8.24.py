def sumaent(n1):
    suma = (n1 * (n1+1))/2
    return suma

entero = int(input("ingresar un entero positivo: "))
print(f"la suma desde el 1 hasta {entero} es {sumaent(entero)}")