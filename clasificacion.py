import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def scatter_group_by(df, x_column, y_column, label_column, file_path):
    plt.figure(figsize=(10, 8))  # Modificar el tamaño de la figura
    labels = pd.unique(df[label_column])
    cmap = plt.cm.get_cmap("hsv", len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        plt.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)  
    plt.savefig(file_path, bbox_inches='tight')  
    plt.close()

def euclidean_distance(p_1, p_2):
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neightbors(points, labels, input_data, k):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        np.unique([labels[index] for index in point_nearest], return_counts=True)[0][0]
        for point_nearest in points_k_nearest
    ]

try:
    df = pd.read_csv(r"C:\Users\alexi\Desktop\mineria de datos\datos_limpio.csv")
except FileNotFoundError:
    print("El archivo no se encontró en la ubicación especificada.")

list_t = [
    (np.array([x, y]), label)
    for x, y, label in zip(df['User Rating Count'], df['Average User Rating'], df['Genres'])
]
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neightbors(
    np.array(points),
    np.array(labels),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5,
)
print(kn)

scatter_group_by(df, 'User Rating Count', 'Average User Rating', 'Genres', 'C:\\Users\\alexi\\Desktop\\mineria de datos\\img\\Classification.png')


def euclidean_distance(p_1, p_2):
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neightbors(points, labels, input_data, k):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        np.unique([labels[index] for index in point_nearest], return_counts=True)[0][0]
        for point_nearest in points_k_nearest
    ]

try:
    df = pd.read_csv(r"C:\Users\alexi\Desktop\mineria de datos\datos_limpio.csv")
except FileNotFoundError:
    print("El archivo no se encontró en la ubicación especificada.")

list_t = [
    (np.array([x, y]), label)
    for x, y, label in zip(df['User Rating Count'], df['Average User Rating'], df['Genres'])
]
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neightbors(
    np.array(points),
    np.array(labels),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5,
)
print(kn)

scatter_group_by(df, 'User Rating Count', 'Average User Rating', 'Genres', 'C:\\Users\\alexi\\Desktop\\mineria de datos\\img\\Classification.png')
