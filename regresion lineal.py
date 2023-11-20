import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
import numpy as np
from tabulate import tabulate
from io import StringIO

def print_tabulate(df: pd.DataFrame):
  print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x: str) -> pd.Series:
  if isinstance(df[x][0], numbers.Number):
      return df[x] # type: pd.Series
  else:
      return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x: str, y: str) -> None:
  fixed_x = transform_variable(df, x)
  model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()
  print(model.summary())

  coef = pd.read_html(StringIO(model.summary().tables[1].as_html()), header=0, index_col=0)[0]['coef']
  df.plot(x=x, y=y, kind='scatter')
  plt.plot(df[x], [df[y].mean() for _ in range(len(df))], color='green')
  plt.plot(df[x], [coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
  plt.xticks(rotation=90)
  plt.savefig(f'img/lr_{y}_{x}.png')
  plt.close()

df = pd.read_csv(r"C:\\Users\\alexi\\Desktop\\mineria de datos\\juegos_de_celular.csv") # type: pd.DataFrame

relevant_columns = ["Average User Rating", "User Rating Count"]
cleaned_df = df.dropna(subset=relevant_columns).replace([np.inf, -np.inf], np.nan).dropna(subset=relevant_columns)

linear_regression(cleaned_df, "Average User Rating", "User Rating Count")
