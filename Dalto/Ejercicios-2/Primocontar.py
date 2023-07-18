#creando una funcion que nos devuelva los 
# numeros primos del 0 al argumento que pasamos

def es_primo(numero): #funcion para definir si es numero primo
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) +1):
        if numero % i == 0: return False
    return True

def primoshasta(limite):
    numeros = []
    for i in range(3,limite+1):
        if es_primo(i) == True: numeros.append(i)
    return numeros

limite = int(input("ingrese hasta que numero entero quiere la lista de los primos: "))
print(primoshasta(limite))


        
        
