# con escribir entre comillas a para append se logra, y w para write
with open("Dalto\\archivos\\texto_de_dalto.txt", "a",encoding="UTF-8") as archivo:
    
    # usando bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f"- recontrato copado {i+1}\n")
        
    # sobre escribiendo el archivo
    # archivo.write("jajajajja te la recontra gane")
    # archivo.writelines(["- hola maestro como andas\n","- Misericordia\n"])
    # writelines se acumula
    # archivo.writelines(["- copado bro\n","- otra linea mas loco\n"])