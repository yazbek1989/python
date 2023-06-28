diccionario1 = {
    "nombre" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 1000000
}

# keys nos muestra todos los nombres de las keys
claves = diccionario1.keys()

# obtenemos un elemento con get() (si no encuentra nada el programa continua, evita la excepcion)
valrod_de_kasdks = diccionario1.get("kasdks")
print("Hola papa, el programa continua")

# clear elimina todo el diccionario
# claves = diccionario1.clear()

# eliminando un elemento del diccionario
diccionario1.pop("nombre")

# obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario1.items()


print(diccionario1)
print(diccionario_iterable)