import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar los datos desde un archivo CSV local
file_path = "C:/Users/alexi/Desktop/mineria de datos/datos_limpio.csv"
df = pd.read_csv(file_path)

# Directorio donde se guardarán las imágenes
directory = "C:/Users/alexi/Desktop/mineria de datos/img"

# Si el directorio no existe, se crea
if not os.path.exists(directory):
    os.makedirs(directory)

# Gráfico de barras para las primeras 15 aplicaciones y sus puntajes promedio de usuarios
df_15 = df.head(15)
fig, ax = plt.subplots()

x = df_15['Name']
y = df_15['Average User Rating']
ax.bar(x, y)

ax.set_xlabel("Aplicaciones")
ax.set_ylabel("Puntaje Promedio de Usuarios")
ax.set_title("Puntajes Promedio de las Primeras 15 Aplicaciones")

plt.xticks(rotation=90)

# Guardar la imagen en la ruta especificada
img_path_1 = os.path.join(directory, 'puntajes_promedio.png')
plt.savefig(img_path_1)
plt.show()

# Gráfico de barras para las primeras 15 aplicaciones y la cantidad de calificaciones de usuarios
fig, ax = plt.subplots()

x = df_15['Name']
y = df_15['User Rating Count']
ax.bar(x, y)

ax.set_xlabel("Aplicaciones")
ax.set_ylabel("Cantidad de Calificaciones de Usuarios")
ax.set_title("Calificaciones de Usuarios de las Primeras 15 Aplicaciones")

plt.xticks(rotation=90)

# Guardar la imagen en la ruta especificada
img_path_2 = os.path.join(directory, 'calificaciones_usuarios.png')
plt.savefig(img_path_2)
plt.show()
