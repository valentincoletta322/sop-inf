import pandas as pd

# Cargar el archivo CSV con codificación 'utf-8'
csv = pd.read_csv("datos.csv", encoding='utf-8')

# Mostrar los primeros registros del DataFrame
print(csv.head())

# valores desconocidos a null
csv['Título'].fillna("Desconocido", inplace=True)
csv['Género'].fillna("Desconocido", inplace=True)
csv['Director'].fillna("Desconocido", inplace=True)
csv['País'].fillna("Desconocido", inplace=True)

# Convertir la columna "Año" a tipo numérico y manejar valores inválidos como NaN
csv['Año'] = pd.to_numeric(csv['Año'], errors='coerce')

csv = csv.drop_duplicates()

# print despues del data cleaning
print("Registros después de rellenar valores nulos:")
print(csv.head())

# Guarda el DataFrame limpio en un nuevo archivo CSV
csv.to_csv("peliculas_limpias.csv", index=False)
