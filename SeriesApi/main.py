import requests
import matplotlib.pyplot as plt
import pandas as pd

url = "https://apis.datos.gob.ar/series/api/series?ids=Automotriz_expos_ItCfsr"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if "data" in data:
        records = data["data"]
        df = pd.DataFrame(records)

        csv_filename = "datos.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Datos guardados en {csv_filename}")



        loaded_df = pd.read_csv(csv_filename)
        print("Contenido del archivo CSV:")
        print(loaded_df)

        data = loaded_df["0"]
        plt.figure(figsize=(10, 5))
        plt.hist(data, bins=4, rwidth=0.9)
        plt.ylim(0, 10)
        plt.title("Grafico")
        plt.show()

else:
    print('Error al obtener los datos. Código de estado:', response.status_code)
