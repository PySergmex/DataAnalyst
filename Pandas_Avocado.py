import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data

#print("Se instalaron los packages correctamente")
#Leer CSV
df = pd.read_csv('./CSV/avocado.csv')
#print(df)
#print(df.head(5))
#Definirel dato que queremos buscar 
chicago = df[df['region'] == 'Chicago']
#print(chicago.head(5)
#Iniciar con la columnada "Date" en la busqueda
chicago = chicago.set_index('Date')
#Ordenar la columna de forma descendente
chicago = chicago.sort_values(by="Date")
#print(chicago.head(5))

#-----------------------------------------------

#Grapic

MAX_SAMPLES = 100

precio = chicago["AveragePrice"][:MAX_SAMPLES]
cantidad = chicago["Total Volume"][:MAX_SAMPLES]


#Nueva grafica
plt.plot(precio, label="Precio Medio")
plt.title("Precio de los aguacates vs tiempo")
plt.xlabel("Fecha")
plt.xticks(rotation=90)
plt.ylabel("Precio $")
plt.legend()
plt.show()

