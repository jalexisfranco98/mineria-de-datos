import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_df(means, n):
    lists = [
        (
            create_distribution(_x, n),
            create_distribution(_y, n),
            np.repeat(_l, n)
        )
        for _x, _y, _l in means
    ]
    x = np.array([])
    y = np.array([])
    labels = np.array([])
    for _x, _y, _l in lists:
        x = np.concatenate((x, _x), axis=None)
        y = np.concatenate((y, _y))
        labels = np.concatenate((labels, _l))
    return pd.DataFrame({"x": x, "y": y, "label": labels})

def k_means(points, k):
    DIM = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, DIM))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0) if np.sum(y == k) > 0 else np.zeros(DIM) # Avoid NaN in case of empty cluster
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp)
    plt.savefig("C:\\Users\\alexi\\Desktop\\mineria de datos\\img\\kmeans.png")
    plt.close()
    return mean

def scatter_group_by(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots()
    labels = df[label_column].unique() if label_column in df.columns else [] # Check if label_column exists
    cmap = plt.cm.get_cmap("hsv", len(labels) + 1) if labels else None # Get cmap if labels exist
    for i, label in enumerate(labels):
        filter_df = df[df[label_column] == label]
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
    plt.close()

data = {
    "Average User Rating": [4, 3.5, 3, 3.5, 3.5, 3, 2.5, 2.5, 2.5, 2.5],
    "User Rating Count": [3553, 284, 8376, 190394, 28, 47, 35, 125, 44, 184],
    "Primary Genre": ["Games", "Games", "Games", "Games", "Games", "Games", "Games", "Games", "Games", "Games"]
}

df = pd.DataFrame(data)
df["Average User Rating"] = df["Average User Rating"].astype(float)
df["User Rating Count"] = df["User Rating Count"].astype(float)

points = np.array(df[['Average User Rating', 'User Rating Count']])
k_means(points, 3)
scatter_group_by("C:\\Users\\alexi\\Desktop\\mineria de datos\\img\\scatter_plot.png", df, "Average User Rating", "User Rating Count", "Primary Genre")
