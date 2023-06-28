contactos = {}
while True:
    usuario = input("por favor ingrese su nombre o 'no' si no quiere ingresar mas: ")
    if usuario == "no":
        break
    elif usuario not in contactos:
        telefono = input("ingrese su numero de telefono: ")
        contactos[usuario] = telefono
    elif usuario in contactos: 
        print("el usuario es repetido")
        
print(contactos)