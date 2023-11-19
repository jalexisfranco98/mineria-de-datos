import pandas as pd
import plotly.graph_objects as go

file_path = "C:/Users/alexi/Desktop/mineria de datos/datos_limpio.csv"
df = pd.read_csv(file_path)  

# Seleccionar columnas relevantes
relevant_columns = [
    'ID', 'Name', 'Average User Rating', 'User Rating Count',
    'Price', 'In-app Purchases', 'Developer', 'Age Rating',
    'Primary Genre', 'Genres', 'Original Release Date',
    'Current Version Release Date'
]


df_LIMP = df[relevant_columns]


df_LIMP_15 = df_LIMP.head(15)

fig = go.Figure()

fig.add_trace(go.Box(y=df_LIMP_15['Average User Rating'], name='Average User Rating'))


fig.add_trace(go.Box(y=df_LIMP_15['User Rating Count'], name='User Rating Count'))


fig.update_layout(
    title={
        'text': "Box Plots - User Ratings",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

fig.show()
