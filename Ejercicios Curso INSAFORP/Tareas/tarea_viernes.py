# Ejercicio 1
cesta_compras = {}
sumar = float(0)

# Pedir información al usuario y añadirla al diccionario
iniciar = True
while iniciar: 
    articulo = input("que articulo quieres comprar o ingrese bye para salir: ")
    if articulo == "bye":
        break
    else:
        valor_articulo = float(input(f"que valor tiene el {articulo}: "))
        cesta_compras[articulo] = valor_articulo
        
print(f"\nla lista de compra es la siguiente: ")
for articulo, valor_articulo in cesta_compras.items():
    print(f"{articulo:<10}{valor_articulo:>10}")
    sumar += valor_articulo
    
print(f"el total es: {sumar:>5}")

# Ejercicio 2
diccionario = {}

# ingresar las palabras con su traduccion ejemplo perro:dog
frase = input("Ingrese las palabras y sus traducciones en formato palabra:traducción, separadas por comas: ")

# se dividen las palabras a una lista
pares = frase.split(',')


for par in pares:
    # se dividen la traduccion de la palabra original
    original, traduccion = par.split(':')
    # se quitan los espacios
    original = original.strip()
    traduccion = traduccion.strip()
    # se agregan al diccionario cada palabra con su traduccion
    diccionario[original] = traduccion

# se ingresa la frase a traducir 
frase = input("Ingrese una frase en español para traducir: ")

# se divide la frase
palabras = frase.split()

# abrir lista para poder ingresar la traduccion ya hecha 
traducido = []
# recorrer cada palabra a traducir
for original in palabras:
    traduccion = diccionario.get(original)
    if traduccion is None:
        # si la palabra no se encuentra se queda igual
        traducido.append(original)
    else:
        # la palabra traducida
        traducido.append(traduccion)

print("Frase traducida:")
# imprimiendo la lista pero sin las comas sustituyendo los espacios por dichas comas
print(' '.join(traducido))

