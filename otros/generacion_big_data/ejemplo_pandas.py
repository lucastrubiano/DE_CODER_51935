import pandas as pd

PATH_ARCHIVO = 'data/datos_iot.csv'

# Crear un DataFrame a partir de un csv
print("Leyendo csv")
df = pd.read_csv(PATH_ARCHIVO, sep='|')

print("Haciendo count")
print(df.count())