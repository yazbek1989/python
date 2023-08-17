import re 

texto = '''Hola maestro, esta es la cadena 1, como estas mi capitan?
Hola esta es la cadena 2 de texto
Hola esta es la cadena 3 de texto'''

resultado = re.search("Hola", texto)
print(resultado)