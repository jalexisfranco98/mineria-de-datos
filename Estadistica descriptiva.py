import pandas as pd
import matplotlib.pyplot as plt


file_path = "C:/Users/alexi/Desktop/mineria de datos/datos_limpio.csv"
df = pd.read_csv(file_path)


df_LIMP = df[['ID', 'Name', 'Average User Rating', 'User Rating Count', 'Price',
               'In-app Purchases', 'Developer', 'Age Rating', 'Primary Genre',
               'Genres', 'Original Release Date', 'Current Version Release Date']]

print(df_LIMP)

mean_rating = df_LIMP['Average User Rating'].mean()
print(f"Promedio de la calificación de usuarios: {mean_rating}")

original_release_stats = df_LIMP['Original Release Date'].describe()
print(f"Estadísticas de fecha de lanzamiento: \n{original_release_stats}")

ruta_imagen = "C:/Users/alexi/Desktop/mineria de datos/img/grafico.png"


plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Ejemplo de Gráfico')
plt.savefig(ruta_imagen)
plt.close()


datos_interesantes = df_LIMP[['ID', 'Name', 'Average User Rating']]

ruta_archivo = "C:/Users/alexi/Desktop/mineria de datos/resultados.txt"
datos_interesantes.to_csv(ruta_archivo, sep='\t', index=False)
