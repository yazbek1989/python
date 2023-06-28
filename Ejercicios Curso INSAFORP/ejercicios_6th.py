# ejercicio 1 funcion que diga hola mundo
def hola():
    print("Hola Mundo")
    
print(hola)
    
# ejercicio 2 Realiza una función que sume dos números pasados por parámetros.

def suma2(a,b):
    return a+b

a = 1
b = 3
print(suma2(a,b))
    
# ejercicio 3 Crea una función que dados dos números mostrará todos los números que hay entre ellos.

def contar_entre(num1,num2):
    if num1 > num2:
        while num1 > num2:
            print(num1)
            num1 -= 1
    else:
        while num1 != num2:
            print(num1)
            num1 += 1

print(contar_entre(10,45))
              
# Ejercicio 4 Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la 
# dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se 
# considerará válida si contiene el símbolo "@".
def verificar_email(email):
    valido = "@" in email
    if valido == True:
        print("el email es valido")
    else:
        print("el email no es valido")
        
verificar_email(input("por favor ingresar su direccion de correo electronico: "))

# Ejercicio 5 Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de 
# sus dígitos (utilizando una función que realice dicha suma)

suma_total = 0
def sumar(numero):
    global suma_total
    suma_total += numero
    return suma_total

conta = None
while conta != 0:
    conta = float(input("por favor ingrese un numero para sumar, si desea salir ingrese 0: "))
    print(sumar(conta))
    
# Ejercicio 6) Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de
# sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de 
# sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.

# def suma2(a,b):
#     return a+b
    
conta = None
sumado = float(0)
while conta != 0:
    conta = float(input("por favor ingrese un numero para sumar, si desea salir ingrese 0: "))
    sumado = suma2(conta, sumado)
    
print(f"{sumado = }")

# Ejercicio 7) Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un 
# número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También 
# solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número 
# (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def sum_digitos(numero):
    sum = 0
    while numero > 0:
        digito = numero % 10
        sum += digito
        numero //= 10
    return sum

def contar_digitos(numero, digito):
    contar = 0
    while numero > 0:
        if numero % 10 == digito:
            contar += 1
        numero //= 10
    return contar

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numeros_primos = []
max_numero = 0

while True:
    numero = int(input("Ingrese un numero primo (o un numero no primo para finalizar): "))
    
    if not primo(numero):
        break
    
    numeros_primos.append(numero)
    if numero > max_numero:
        max_numero = numero
    
    digito = int(input("ingrese un digito: "))
    frecuencia_digito = contar_digitos(numero, digito)
    print(f"la suma de los digitos de {numero} es: {sum_digitos(numero)}")
    print(f"El digito {digito} aparece {frecuencia_digito} veces en el numero {numero}\n")
    
if max_numero > 0:
    max_factorial = factorial(max_numero)
    print(f"El factorial del mayor numero ingresado {max_numero} es: {max_factorial}")
else:
    print("No se ingresaron numeros primos")
    


    
    

# Ejercicio 8) El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 
# pero en su lugar imprime 5. ¿Qué hay que corregir?

def maximo(a,b):
    if a>b:
        return a
    else:
        return b
    
def minimo(a,b):
    if a<b:
        return a
    else:
        return b

#programa principal
x=int(input("un numero: "))
y=int(input("otro numero: "))
print(maximo(x-3, minimo(x+2,y-5)))

# Ejercicio 9) El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 
# pero en su lugar imprime 5. ¿Qué hay que corregir?
# ingresar 6 y 7 y el resultado coordenadas 8 y 9

def coordenadaz(x,y):
    x=x+10
    y=y+15
    return x+y

# programa principal
x=int(input("Coordenada eje x: "))
y=int(input("coordenada eje y: "))
for i in range(2):
    #z=coordenadaz(x,y)
    #print(z)
    x=x+1
    y=y+1
print(x," . ",y)
    
