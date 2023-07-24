# con el as se iguala para poder usar el open
with open("Dalto\\archivos\\texto_de_dalto.txt", encoding="UTF-8") as archivo:
    
    # leemos el archivo
    contenido = archivo.read()
    
    # mostramos el archivo
    print(contenido)
    
# no es necesario cerrarlo al usar with open