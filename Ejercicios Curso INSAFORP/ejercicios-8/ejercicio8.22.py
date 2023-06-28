""" 22. Escriba un programa que pida dos años y escriba cuántos años bisiestos hay entre esas dos 
fechas (incluidos los dos años): """
def es_bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year_inicial = int(input("Ingrese el año inicial: "))
year_final = int(input("Ingrese el año final: "))

cantidad_bisiestos = 0

for year in range(year_inicial, year_final + 1):
    if es_bisiesto(year):
        cantidad_bisiestos += 1

print("Cantidad de años bisiestos entre", year_inicial, "y", year_final, ":", cantidad_bisiestos)
