import re 

texto = '''Hola maestro, Esta es la cadena 1. como estas mi capitan?
Hola esta es la cadena 255,255,255 de texto.
Hola esta es la cadena 255 de texto.'''

# haciendo una busqueda simple
# resultado = re.findall("esta", texto, flags=re.IGNORECASE)

#\d -> busca digitos numeros del 0 al 9 
# resultado = re.findall(r"\d",texto)

#\D -> busca todo menos numeros porque ahora es mayuscula 
# resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _] 
# resultado = re.findall(r"\w",texto)

#\W -> busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _] 
# resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco, tabs, y saltos de linea 
# resultado = re.findall(r"\s",texto)

#\S -> busca todo menos espacios en blanco, tabs, y saltos de linea 
# resultado = re.findall(r"\S",texto)

#. busca todo menos saltos en linea
# resultado = re.findall(r".",texto)

#\n busca saltos en linea
# resultado = re.findall(r"\n.",texto)

#\ cancelar caracteres especiales para busqueda de caracteres especiales jajajaj
# resultado = re.findall(r'\.',texto)

# armando una cadena que busque un numero, seguido de un punto y un espacio
# resultado = re.findall(r'\d\.\s',texto)

# ^ buscando el comienzo de una linea, buscando hola en el principio de una linea
# resultado = re.findall(r'^Hola', texto, flags=re.M)

# $ buscando el final de una linea, buscando texto en el final de una linea
# resultado = re.findall(r'texto.$', texto, flags=re.M)

# {n} busca n cantidad de veces el valor de la izquierda
# resultado = re.findall(r'\d{3}\s', texto)

# {n,m} rango al menos como n maximo como m. entre parentesis si queremos buscar un conjunto. entre corchete [] si queremos buscar lo que esta adentro varias veces
# resultado = re.findall(r'(ab){1,3}', texto)

# | busca una cosa o la otra es condicion
resultado = re.findall(r'\d{1,3}|Hola', texto)


print(resultado)