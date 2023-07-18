# Ejercicio 2: zip
# Imagina que tienes dos listas, una con nombres y otra con edades, y quieres combinarlos en pares de (nombre, edad). Puedes utilizar la función zip para lograrlo:

nombres = ["Ivan", "Kaisy", "Luisa"]
edad = [33,31, 68]
nombre_edad = dict(zip(nombres,edad))
print(nombre_edad)