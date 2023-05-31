import pandas as pd

# Cargar el archivo CSV con codificación 'utf-8'
csv = pd.read_csv("carreras.csv", encoding='utf-8')

# Eliminar filas con valores nulos o vacíos
csv.dropna(inplace=True)

# Restablecer los índices del DataFrame
csv.reset_index(drop=True, inplace=True)

# Mostrar el contenido del DataFrame limpio en la terminal
print(csv)

# Guardar el DataFrame limpio en un nuevo archivo CSV
csv.to_csv("carreras_limpias.csv", index=False)
