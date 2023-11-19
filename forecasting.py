import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate
from typing import Tuple, Dict
import numpy as np

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x: str) -> pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x: str, y: str) -> Dict[str, float]:
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()
    bands = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]
    print_tabulate(pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0])
    coef = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]['coef']
    r_2_t = pd.read_html(model.summary().tables[0].as_html(), header=None, index_col=None)[0]
    return {
        'm': coef.values[1],
        'b': coef.values[0],
        'r2': r_2_t.values[0][3],
        'r2_adj': r_2_t.values[1][3],
        'low_band': bands['[0.025'][0],
        'hi_band': bands['0.975]'][0]
    }

def plt_lr(df: pd.DataFrame, x: str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: Tuple[str,str]):
    fixed_x = transform_variable(df, x)
    df.plot(x=x, y=y, kind='scatter')
    plt.plot(df[x], [m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x], [m * x + low_band for _, x in fixed_x.items()], [m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])

try:
    df = pd.read_csv("C:\\Users\\alexi\\Desktop\\mineria de datos\\datos_limpio.csv")
except FileNotFoundError:
    print("El archivo no se encontró en la ubicación especificada.")

df_by_genres = df.groupby("Genres").size().reset_index(name="Count")
print(df_by_genres)

a = linear_regression(df_by_genres, "Genres", "Count")
plt_lr(df=df_by_genres, x="Genres", y="Count", colors=('red', 'orange'), **a)

plt.xticks(rotation=90)
plt.savefig('C:\\Users\\alexi\\Desktop\\mineria de datos\\img\\forecast.png')
plt.close()
