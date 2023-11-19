import pandas as pd

# Cargar el DataFrame desde el archivo CSV local
file_path = "C:/Users/alexi/Desktop/mineria de datos/juegos_de_celular.csv"
df = pd.read_csv(file_path)

# Crear un nuevo DataFrame con las columnas requeridas sin 'Languages'
df_clean = df[['ID', 'Name', 'Average User Rating', 'User Rating Count', 'Price',
               'In-app Purchases', 'Developer', 'Age Rating', 'Primary Genre',
               'Genres', 'Original Release Date', 'Current Version Release Date']]

# Guardar el nuevo DataFrame como archivo CSV en la ubicación especificada
ruta_guardado = "C:/Users/alexi/Desktop/mineria de datos/datos_limpio.csv"
df_clean.to_csv(ruta_guardado, index=False)

# Verificar el nuevo DataFrame resultante
print(df_clean)
