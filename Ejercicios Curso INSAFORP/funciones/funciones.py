""" def prueba (**variable):
    print(f"hoy tenemosa para probar")
    for varia in variable:
        valor = variable[varia]
        print(f"la prueba es imprimir todas las variaciones: {varia} y el valor es: {valor}")
    return

prueba(Nombre = "test", otro = "prueba", numero = 123456) """

# una funcion se puede dejar documentada y detallada con los """ y poner el comentario o explicacion de la funcion """ y esta saldra de ayuda cuando la estemos usando *.* (lo maximo jajajajaj)
def area_triangulo(base, altura):
    """Función que calcula el área de un triángulo.

    Parámetros:
    - base: Un número real con la base del triángulo.
    - altura: Un número real con la altura del triángulo.
    \nSalida:\n
    Un número real con el área del triángulo de base y altura especificadas.
    """
    return base * altura/2

def factorial(n):
    """ ejemplo de funcion recursiva """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

from functools import reduce

print(f"El resultado es: {reduce(lambda n, m: n * m, range(1,5))}")


    


