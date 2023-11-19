import pandas as pd
import plotly.graph_objects as go
import os

# Cargar una muestra de datos desde la ubicación local
file_path = "C:/Users/alexi/Desktop/mineria de datos/datos_limpio.csv"
df = pd.read_csv(file_path)

# Seleccionar columnas relevantes
relevant_columns = [
    'ID', 'Name', 'Average User Rating', 'User Rating Count',
    'Price', 'In-app Purchases', 'Developer', 'Age Rating',
    'Primary Genre', 'Genres', 'Original Release Date',
    'Current Version Release Date'
]

# Crear DataFrame con las columnas seleccionadas
df_LIMP = df[relevant_columns]

# Seleccionar las primeras 15 filas
df_LIMP_15 = df_LIMP.head(15)

# Crear el gráfico con Plotly
fig = go.Figure()

# Box Plot para 'Average User Rating'
fig.add_trace(go.Box(y=df_LIMP_15['Average User Rating'], name='Average User Rating'))

# Box Plot para 'User Rating Count'
fig.add_trace(go.Box(y=df_LIMP_15['User Rating Count'], name='User Rating Count'))

# Configurar el diseño del gráfico
fig.update_layout(
    title={
        'text': "Box Plots - User Ratings",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

# Directorio donde se guardarán las imágenes
directory = "C:/Users/alexi/Desktop/mineria de datos/img"

# Si el directorio no existe, se crea
if not os.path.exists(directory):
    os.makedirs(directory)

# Guardar el gráfico en la ubicación especificada
img_path = os.path.join(directory, 'boxplots_plotly.png')
fig.write_image(img_path)
