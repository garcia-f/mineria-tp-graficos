import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('top-1000-peliculas.csv')

# Limpiar la columna 'Budget (in $)' eliminando cualquier carácter que no sea un dígito o un punto decimal
df['Budget (in $)'] = df['Budget (in $)'].replace('[^\d.]', '', regex=True)

# Convertir la columna 'Budget (in $)' a tipo numérico
df['Budget (in $)'] = pd.to_numeric(df['Budget (in $)'], errors='coerce')

# Eliminar las filas con valores NaN en la columna 'Budget (in $)'
df = df.dropna(subset=['Budget (in $)'])

# Seleccionar las columnas de interés para el gráfico
subset = df[['Title', 'Budget (in $)']]

# Ordenar los datos por presupuesto de forma descendente y tomar los primeros 10 registros
subset_sorted = subset.sort_values(by='Budget (in $)', ascending=False).head(10)

# Crear el gráfico de barras
plt.figure(figsize=(10,6))
plt.barh(subset_sorted['Title'], subset_sorted['Budget (in $)'], color='skyblue')
plt.xlabel('Presupuesto (en $)')
plt.ylabel('Película')
plt.title('Top 10 Películas por Presupuesto')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar la película con el mayor presupuesto en la parte superior
plt.show()
