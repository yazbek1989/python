def area_circulo(radio):
    area = 3.141592 * radio**2
    return area

def volumen_cilindro(radio, altura):
    volumen = 3.141592 * radio**2 * altura
    return volumen

radio_circulo = 7
area_circulo = area_circulo(radio_circulo)
print(f"El área del círculo con radio {radio_circulo} es {area_circulo:.2f}")

radio_cilindro = 5
altura_cilindro = 15
volumen_cilindro = volumen_cilindro(radio_cilindro, altura_cilindro)
print(f"El volumen del cilindro con radio {radio_cilindro} y altura {altura_cilindro} es {volumen_cilindro:.2f}")