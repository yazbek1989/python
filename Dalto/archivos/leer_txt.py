
#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo_sin_leer = open("Dalto\\archivos\\texto_de_dalto.txt", encoding="UTF-8")
# archivo = archivo_sin_leer.read()

#leer linea por linea
# linea_1 = archivo_sin_leer.readlines()

#leer una soloa linea
linea_1 = archivo_sin_leer.readline()

# cerrar el archivo
archivo_sin_leer.close()

print(linea_1)