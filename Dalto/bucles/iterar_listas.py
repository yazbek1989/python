# el bucle for itera el solo hasta acabar la lista
animales = ["perro", "gato", "loro", "Cocodrilo"]
numeros = [10,62,12,72]

# recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")
 
# recorriendo la lista numeros y multiplicando este valor * 10   
for numero in numeros:
    resultado = numero * 10
    print(resultado)

# iterando dos listas al mismo tiempo, tienen que ser del mismo tamaño    
for numero,animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")


for num in range(5,10):
    print(num)    
    
print(f"Un  vale {1.12}$")