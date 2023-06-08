cadena1 = "Hola soy dalto, Hola maquinola"
cadena2 = "bienvenido maquinola"

# coniverte en mayusculas
mayusc = cadena1.upper()

# convierte en minusculas
minusc = cadena1.lower()

# primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("0")

# buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
# busqueda_index = cadena1.index("1")

#si es numero devuelve true, si no, devuelve false
es_numerico = cadena1.isnumeric()

# si es alfanumerico devuelve true, de lo contrario false (solo toma de la a a la z sin contar espacios)
es_alfa = cadena1.isalpha()

# prueba de count, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("Hola")

# len es funcion cuenta la cantidad de caracteres de una cadena
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada 
empieza_con = cadena1.startswith("Hola")

# verificamos si una cadena termina con otra cadena dada 
termina_con = cadena1.endswith("nola")

# reemplaza un pedazo de la cadena dada por otra dada
cadena_nueva = cadena1.replace("Hola","Holu")
cadena_nueva_2 = cadena_nueva.capitalize()

# separar cadenas con la cadena que le pasemos y la pone en lista (datos compuestos)
cadena_separada = cadena1.split(",")

print(cadena_separada[0])