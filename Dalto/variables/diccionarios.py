# creando diccionarios con dict(), solo con esta funcion podemos crear diccionarios vacios
diccionario1 = dict(nombre="lucas", apellido="dalto")
# diccionario = {'nombre':"lucas", "apellido": "dalto"}
print(diccionario1)

# puedo tener como clave una tupla y con frozenset() tambien
diccionario_clave_tupla = {("uno","dos"):"valor"}

print(diccionario_clave_tupla)

# creando diccionarios con fromkeys(), itera el primer elemento del diccioanrio, entonces metamole una lista, el segundo dato que ingresamos es el valor que le da a todas las keys iteradas
diccionario = dict.fromkeys(["nombre","apellido"])

print(diccionario)
