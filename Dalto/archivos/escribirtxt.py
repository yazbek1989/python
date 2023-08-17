with open("Dalto\\archivos\\texto_de_dalto.txt", "w",encoding="UTF-8") as archivo:
    
    # sobre escribiendo el archivo
    # archivo.write("jajajajja te la recontra gane")
    archivo.writelines(["- hola maestro como andas\n","- Misericordia\n"])
    # writelines se acumula
    archivo.writelines(["- copado bro\n","- otra linea mas loco\n"])