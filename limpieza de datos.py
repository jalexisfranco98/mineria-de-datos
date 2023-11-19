import pandas as pd


file_path = "C:/Users/alexi/Desktop/mineria de datos/juegos_de_celular.csv"
df = pd.read_csv(file_path)

df_clean = df[['ID', 'Name', 'Average User Rating', 'User Rating Count', 'Price',
               'In-app Purchases', 'Developer', 'Age Rating', 'Primary Genre',
               'Genres', 'Original Release Date', 'Current Version Release Date']]

ruta_guardado = "C:/Users/alexi/Desktop/mineria de datos/datos_limpio.csv"
df_clean.to_csv(ruta_guardado, index=False)

print(df_clean)
