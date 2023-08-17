import pandas as pd

# Data Frame son estructuras de datos, filas y columnas , names=["name","lastname","age"] 'asi podemos asignar nombre a la columna y que tome como dato desde el valor 0 del archivo'
df = pd.read_excel(r"Dalto\archivos\Base de Proveedores.xlsx")

#parametros para ordenar el dataframe, con ascending solo en el caso de false y sort_values
df = df.sort_values("Razón Social", ascending=False)

#obteniendo los datos de la columna razon social
nombres = df["Razón Social"]

# convertir a string los datos de una columna
df['Razón Social'] = df['Razón Social'].astype(str)

# para concatenera Data frames se usa df_concatenado = pd.concat([df1, df2])
# df.head(4) muestra la fila contando de arriba hacia abajo de la 1 a la 4
# df.tail(4) muestra la fila contando de abajo hacia arriba de la 1 a la 4 contando al revez

# df.shape cuenta la cantidad de filas y columnas en ese orden y lo devuelve en forma de tupla
df_filas, df_columnas = df.shape

print(f"la cantidad de filas son {df_filas}")
print(f"las columnas son: {df_columnas}")

# accediendo a la columna razon social de la fila 4
elemento_especifico_loc = df.loc[4,"Razón Social"]
print(elemento_especifico_loc)

# accediendo a toda la fila 4
elemento_especifico_iloc = df.iloc[4,:]
print(elemento_especifico_iloc)

# buscando credenciales vencidas
distrito_filtro = df.loc[df["Distrito"]=="ZARAGOZA",:]
print(f"las empresas con el distrito de zaragoza son las siguientes \n")
print(distrito_filtro)

# df.describe() sirve para dar informacion general de los datos del archivo

#slicing 6:28 del video
print(nombres[1:10])

# .dropna(axis=1) es para columnas, vacio es para filas con datos faltantes, .replace("dalto","maestro",inplace=True), .drop_duplicates()

# df.to_excel(r"Dalto\archivos\Base de Proveedores.xlsx") creando nuevo archivo con cambios hechos