edad = int(input("que edad tiene: "))
ingreso = float(input("cual es su ingreso mensual: $"))
if edad > 16: 
    if ingreso >= 1000:
       print("tiene que tributar")
    else:
        print("no tiene que tributar")
else:
    print("no tiene que tributar")
