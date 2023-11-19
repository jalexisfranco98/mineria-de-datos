import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

def scatter_group_by(file_path, df, x_column, y_column, label_column):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = plt.cm.get_cmap("hsv", len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
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
        mode([labels[index] for index in point_nearest])
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


def k_nearest_neightbors(points, labels, input_data, k):
    input_distances = [
        [np.linalg.norm(input_point - point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        np.unique([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]

kn = k_nearest_neightbors(
    np.array(points),
    np.array(labels),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5,
)
print(kn)