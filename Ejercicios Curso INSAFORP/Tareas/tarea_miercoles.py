# ejercicio 1
# calcular el area de un circulo con su radio

pi = 3.141592
radio = float(input("Escribe el valor del radio: "))
area = pi*radio**2
print(f"el area del circulo es igual a {area:0.2f}")

# ejercicio 2
# calcular el volumen de una esfera con el radio dado

pi = 3.141592
radio = float(input("por favor ingrese el radio de la esfera: "))
volumen = (4/3)*pi*radio**3
print(f"el volumen de la esfera es igual a: {volumen:.2f}")

# ejercicio 3
# obtener un conjunto de numeros separados por , y crear una lista de estos

entrada = input("escriba varios numeros separados por ',': ")
numeros_lista = entrada.split(",")
print(f"los datos de la lista son los siguientes: {numeros_lista}")

# ejercicio 4
# conocewr el primero, el tercero y el ultimo de una lista 

lenguajes = ['PYTHON', 'C#', 'PHP', 'JAVA', 'JAVASCRIPT']
print(f"El primer lenguaje es: {lenguajes[0]}, el tercer lenguaje es: {lenguajes[2]}, y el ultimo lenguaje es {lenguajes[-1]}")
print(f"El primer lenguaje es: {lenguajes[-5]}, el tercer lenguaje es: {lenguajes[-3]}, y el ultimo lenguaje es {lenguajes[-1]}")


