import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

file_path = "C:/Users/alexi/Desktop/mineria de datos/juegos_de_celular.csv"
df = pd.read_csv(file_path)

relevant_columns = ['User Rating Count', 'Average User Rating']
df_LIMP = df[relevant_columns]

df_LIMP = df_LIMP.dropna()  # Eliminar filas con valores faltantes
df_LIMP = df_LIMP.replace([float('inf'), -float('inf')], pd.NA).dropna()

x = df_LIMP['User Rating Count']
y = df_LIMP['Average User Rating']
x = sm.add_constant(x)  

model = sm.OLS(y, x).fit()  
print(model.summary())  

plt.scatter(df_LIMP['User Rating Count'], df_LIMP['Average User Rating'], alpha=0.5)
plt.xlabel('User Rating Count')
plt.ylabel('Average User Rating')

plt.plot(df_LIMP['User Rating Count'], model.predict(x), color='red')

img_path = "C:/Users/alexi/Desktop/mineria de datos/img/regresion.png"
plt.savefig(img_path)
plt.show()




