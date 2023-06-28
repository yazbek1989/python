"""
4. Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las 
facturas se almacenarán en un diccionario donde la clave de cada factura será el número 
de factura y el valor el coste de la factura. El programa debe preguntar al usuario si 
quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una 
nueva factura se preguntará por el número de factura y su coste y se añadirá al 
diccionario. Si se desea pagar una factura se preguntará por el número de factura y se 
eliminará del diccionario. Después de cada operación el programa debe mostrar por 
pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro
"""
factura = {}
cobrado = 0
pendiente = 0
while True:
    entrada = input("quiere 'anadir' factura, 'pagar' una existente o 'terminar':")
    if entrada == "terminar":
        break
    elif entrada == "anadir":
        numero_fac = input("cual es el numero de factura: ")
        costo_fac = float(input("cual es el costo de la factura: "))
        factura[numero_fac] = costo_fac
        pendiente += costo_fac
    elif entrada == "pagar":
        pagar_fac = input("cual es el numero de factura que quiere pagar: ")
        cobrado += factura[pagar_fac]
        pendiente -= factura[pagar_fac]
        factura.pop(pagar_fac)
        print(f"el total pagado es: {cobrado:.2f}")
    else:
        print("por favor ingrese una de las opciones")
    print(f"la cantidad pendiente de pagar es {pendiente:.2f}")    
    