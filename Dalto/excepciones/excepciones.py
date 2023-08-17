def sumar_dos():
    '''Esta funcion suma dos numeros y si se mete algo que no sea numero entero manda un mensaje diciendo que esta mal lo que metiste'''
    while True:  
        a = input("Numero 1: ")
        b = input("Numero 2: ")  
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            print("te pedi un numero no un texto")
            print(f"el error es {e}")
            print(type(e).__name__)
        else: 
            break
        finally:
            print("esto se ejecuta siempre(manejo de excepcion finalizado)")
    return resultado
    
print(sumar_dos())