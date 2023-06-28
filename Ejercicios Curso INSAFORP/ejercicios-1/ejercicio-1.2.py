# guarda el input en la variable frase
frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

# dividir por espacios las palabras y pasarlos a una lista
palabras_separadas = frase.split(" ")

# contar el largo de la lista generado por el split
cantidad_de_palabras = len(palabras_separadas)

# calcular cuantas palabras por segundo puede decir la persona
print(f"dijiste {cantidad_de_palabras} y tardarias {cantidad_de_palabras/2}s en decirlo")

# redondear el dato de los segundos gnerados y decir cuanto tardaria dalto
print(f"dalto tardaria {round(cantidad_de_palabras/2*0.7,2)}s en decirlo")

if cantidad_de_palabras > 180:
    print("para flaco tampoco pedi un testamento jajajaja")
else:
    print("por lo menos no hiciste un testamento")