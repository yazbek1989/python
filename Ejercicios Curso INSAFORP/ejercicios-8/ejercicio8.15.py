
"""
15. Crear un programa que solicite el ingreso de números enteros positivos, 
hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares 
y cuántos impares tiene. Al finalizar, 
informar la cantidad de dígitos pares y de dígitos impares leídos en total."""
def digito_par_impar(numero):
    par = 0
    impar = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            par += 1
        else:
            impar += 1
        numero //= 10
    return par, impar
    
par = 0
impar = 0
numero = 1
while numero !=0:
    numero = int(input("ingrese un entero positivo o '0' para salir: "))   
    dig_par, dig_impar = digito_par_impar(numero)
    print(f"{numero} tiene {dig_par} digitos pares, y {dig_impar} digitos impares")
    par += dig_par
    impar += dig_impar   
     
print(f"la cantidad de numeros pares leidos fue de {par} y de impares de {impar}")
    
    