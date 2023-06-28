#falto el profe y los pibes van a dar la clase

# pedir el nombre y la edad de los compañeros que llegaron a clase

def obtener_compas(cantidad):
    companeros = []    
    for i in range(cantidad):
        nombre = input("Nombre del Alumno: ")
        edad = int(input("Que edad tiene: "))
        companero = (nombre, edad)
        companeros.append(companero)
    companeros.sort(key=lambda x:x[1])
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_compas(5)
print(f"El profesor es: {profesor} y el asistente es: {asistente}")
