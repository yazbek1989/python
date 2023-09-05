import re

# cadena en la que se buscaran los patrones
text = "la fecha es 23/06/2021 y 01/09/2023, el telefono es +1-555-555-5555"

# este es el patron de reemplazo
pattern = r"\d{2}/\d{2}/\d{4}"

# este es por lo cual lo vamos a reemplazar
replacement = "Fecha Oculta"

# esta es el objeto que usaremos para hacer el reemplazo de todas las apariciones
new_text = re.sub(pattern,replacement,text)


print(new_text)