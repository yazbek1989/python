#contar primos hasta x numero e imprimirlos, con dos funciones lambda anidadas
primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5)+1)), range(2, num+1)))
#imprimir primos
print(primos_hasta(13))