import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./CSV/avocado.csv')

atlanta = df[df["region"]=="Atlanta"]

precio = atlanta["AveragePrice"]
precio_average = precio.rolling(25, min_periods=1).mean()
print(precio[:30])
print(precio_average[:30])
volumen = atlanta["Total Volume"]

bolsasAguacate = atlanta["Total Bags"]
sbolsas = atlanta["Small Bags"]
lbolsas = atlanta["Large Bags"]
xlbolsas = atlanta["XLarge Bags"]


plt.subplot(221)
plt.title("Precio aguacate")
plt.plot(precio, label="Precio", color="green")
plt.plot(precio_average, label="Precio promediado", color="red")
plt.legend()

plt.subplot(222)
plt.title("Volumen de aguacates")
plt.plot(volumen, label="Volumen Total", color="red")
plt.legend()

plt.subplot(223)
plt.title("Bolsas de Aguacates Totales")
plt.plot(bolsasAguacate, label="Bolsas Totales", color="blue")
plt.legend()

plt.subplot(224)
plt.title("Bolsas por tamaño")
plt.plot(sbolsas, label="Pequeñas", color="black")
plt.plot(lbolsas, label="Medianas", color="cyan")
plt.plot(xlbolsas, label="Grandes", color="yellow")
plt.legend()

plt.tight_layout()
plt.show()