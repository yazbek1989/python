lista = [0]*10
for i in range(10):
    numero = float(input("ingrese un numero: "))
    lista[i] = numero
    
print(lista)
suma = sum(lista)
media = suma / len(lista)
print(f"la suma de la lista es: {suma:.2f}")
print(f"la media de la lista es: {media:.2f}")    

