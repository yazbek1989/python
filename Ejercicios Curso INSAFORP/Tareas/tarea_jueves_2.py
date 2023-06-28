""" 
Ejercicio 1
Escribir un programa que guarde en un diccionario los precios de las frutas de la 
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla 
el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe 
mostrar un mensaje informando de ello. 
"""
# Definición del diccionario de frutas y sus precios
frutas = {
    'Platano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}

while True:
    try:
        Fruta = input("Ingrese la fruta a comprar o escriba Salir: ")
        if Fruta == "Salir":
            break
        else:
            Fruta = Fruta.capitalize()
            valor = frutas[Fruta]
            kgs = float(input(f"Ingrese la cantidad en kilos de {Fruta}: "))
            precio = kgs * valor
            print(f"El precio de {kgs} kgs de {Fruta} es: {precio:.2f}")
            break
    except KeyError:
        print("Error: Ingrese una fruta válida: ")
        print(", ".join(frutas.keys()))

"""
Ejercicio 2
Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo 
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato 
debe imprimirse el contenido del diccionario. 
"""
# Crear un diccionario vacío
persona = {}

# Pedir información al usuario y añadirla al diccionario
iniciar = True
while iniciar: 
    solicitud = input("que queres introducir: ")
    soli_valor = input(f"que {solicitud} es: ")
    persona[solicitud] = soli_valor
    print(persona)
    iniciar = input("quieres agregar mas datos? (si/no)") == "si"

""" 
Ejercicio 3
Escribir un programa que pregunte al usuario su nombre, edad, dirección y 
teléfono y lo guarde en un diccionario. Despúes debe mostrar por pantalla el 
mensaje <nombre> tiene <edad> años, vive en <dirección> y su número 
de teléfono es <teléfono>. 
"""
persona = {}
nombre = input("por favor ingresar el nombre: ")
edad = float(input("ingresar la edad: "))
direccion = input("ingresar direccion: ")
telefono = input("ingresar un # de telefono: ")
persona = {"Nombre":nombre, "Edad": edad, "Direccion": direccion, "Telefono": telefono}
print(f"el nombre es: {persona['Nombre']}, \n la edad es: {persona['Edad']}, \n el telefono es: {persona['Telefono']}\n y la direccion es: {persona['Direccion']}")
