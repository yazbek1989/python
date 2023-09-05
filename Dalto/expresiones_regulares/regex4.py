import re

email = "example@example.com"

# el % es comodin y el + es como el * solo que devuelve coincidencias de 1 en adelante
# el {2,} es para encontrar al menos dos veces en adelante sin limite
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# es para buscar si coincide los dos datos
result = re.match(pattern, email)

if result:
    print("Dirección de correo válida")
else:
    print("Dirección de correo inválida")