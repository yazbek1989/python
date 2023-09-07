""" class Celular():
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"
    
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular() """

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca #+ " hola" se puede agregar a la variable un texto con el simbolo "+" como concatenar
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"has llamado desde un {self.marca} modelo {self.modelo}")
        
    def cortar(self):
        print("has cortado la llamada")
        
        
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 Pro","96MP")
    
celular1.llamar()
celular2.cortar()
