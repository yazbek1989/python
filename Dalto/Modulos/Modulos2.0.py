""" import sys

sys.path.append("C:\\Users\\yazbe\\OneDrive\\Documentos\\Python\\python-1\\Funciones_buenas")
print(sys.path)

import Saludar #da error pero si lo importa igual por el path.append, pero solo funciona para esta instancia

Saludar.Saludar_raro("dalto") """

# Si el modulo estuviera en una carpeta abajo en la ruta se usa . de division
# import Funciones_buenas.Saludar as m_saludar

# m_saludar.Saludar("Dalto")

import paquete.saludar

paquete.saludar.Saludar("dalto")

