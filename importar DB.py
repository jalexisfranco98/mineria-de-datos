import pandas as pd

# Ruta del archivo CSV en tu sistema local
file_path = "C:\\Users\\alexi\\Desktop\\mineria de datos\\juegos_de_celular.csv"

# Leer el archivo CSV
df = pd.read_csv(file_path)

# Mostrar los primeros registros para verificar que se ha cargado correctamente
print(df.head())
