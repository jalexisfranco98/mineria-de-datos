import pandas as pd
from tabulate import tabulate
from typing import Tuple, List

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def calculate_game_metrics(file_name: str) -> Tuple[pd.Series, float, pd.DataFrame]:
    df = pd.read_csv(file_name)
    # Estadísticas de User Rating Count
    user_rating_stats = df['User Rating Count'].describe()
    
    # Precio promedio de los juegos
    avg_price = df['Price'].mean()
    
    # Juegos con la calificación más baja (menor a 2 puntos)
    low_rated_games = df[df['Average User Rating'] < 2]
    
    return user_rating_stats, avg_price, low_rated_games


user_rating_stats, avg_price, low_rated_games = calculate_game_metrics("C:/Users/alexi/Desktop/mineria de datos/datos_limpio.csv")

print("Estadísticas de User Rating Count:")
print_tabulate(user_rating_stats.to_frame().T)

print(f"Precio promedio de los juegos: {avg_price}")

print("Juegos con calificación baja (menor a 2 puntos):")
print_tabulate(low_rated_games[['ID', 'Name', 'Average User Rating']])

# Guardar los resultados en un archivo CSV
user_rating_stats.to_csv("C:/Users/alexi/Desktop/mineria de datos/user_rating_stats.csv", index=False)
low_rated_games.to_csv("C:/Users/alexi/Desktop/mineria de datos/low_rated_games.csv", index=False)
