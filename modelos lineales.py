import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

# Cargar la base de datos
file_path = "C:/Users/alexi/Desktop/mineria de datos/juegos_de_celular.csv"
df = pd.read_csv(file_path)

# Seleccionar las columnas relevantes
relevant_columns = ['User Rating Count', 'Average User Rating']
df_LIMP = df[relevant_columns]

# Limpiar los valores faltantes e infinitos
df_LIMP = df_LIMP.dropna()  # Eliminar filas con valores faltantes
df_LIMP = df_LIMP.replace([float('inf'), -float('inf')], pd.NA).dropna()

# Realizar la regresión lineal
x = df_LIMP['User Rating Count']
y = df_LIMP['Average User Rating']
x = sm.add_constant(x)  # Añadir una constante para el término independiente

model = sm.OLS(y, x).fit()  # Ajustar el modelo
print(model.summary())  # Imprimir los resultados del modelo

# Gráfico de dispersión y línea de regresión
plt.scatter(df_LIMP['User Rating Count'], df_LIMP['Average User Rating'], alpha=0.5)
plt.xlabel('User Rating Count')
plt.ylabel('Average User Rating')

# Línea de regresión
plt.plot(df_LIMP['User Rating Count'], model.predict(x), color='red')

# Guardar la figura
img_path = "C:/Users/alexi/Desktop/mineria de datos/img/regresion.png"
plt.savefig(img_path)
plt.show()




