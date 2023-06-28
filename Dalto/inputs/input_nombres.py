# pedirle un dato al usuario, input siempre da letras no numeros
nombre = input("che maestro, dame tu nombre: ")

# cuando es un numero el que se recibe 
# hay que convertirlo a float() y despues a int()
# dependiendo para poder hacer operaciones matematicas de lo contrario al ser letras 6 * 2 sera igual a 66 jajajaja en vez de 12

# mostrando el dato
print(f"el nombre es: {nombre}")