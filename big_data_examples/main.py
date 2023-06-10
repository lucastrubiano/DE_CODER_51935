# Este es un script para crear tablas con gran cantidad de registros

import random
import os
from datetime import datetime, timedelta

PATH_ARCHIVO = 'data/datos_iot.csv'
FORMATO_ID = 'sensor_{:08d}'
CANT_DISPOSITIVOS_IOT = 1000000 # 1 millon
CANT_DIAS = 365*2 # 2 años

COLUMNAS_TABLA = ['id_dispositivo', 'fecha', 'temperatura', 'humedad', 'presion', 'latitud', 'longitud']
TIPOS_DATOS_TABLA = ['int', 'date', 'float', 'float', 'float', 'float', 'float']
SEPARADOR = '|'

ANIO_INICIO = 2020
MES_INICIO = 1
DIA_INICIO = 1

# Función para generar un registro aleatorio
def generar_registro(id_dispositivo, fecha):
    temperatura = random.uniform(20, 30)
    humedad = random.uniform(40, 60)
    presion = random.uniform(800, 1200)
    latitud = random.uniform(-90, 90)
    longitud = random.uniform(-180, 180)
    
    # return SEPARADOR.join(map(lambda x: str(x), valores)) + '\n'
    return f'{FORMATO_ID.format(id_dispositivo)}|{fecha}|{temperatura}|{humedad}|{presion}|{latitud}|{longitud}\n'

# Función para obtener el número de días de un mes
def obtener_dias_mes(mes, año):
    # Obtener el primer día del mes siguiente
    primer_dia_siguiente_mes = datetime(año, mes, 1) + timedelta(days=32)
    # Restar un día para obtener el último día del mes actual
    ultimo_dia_mes = primer_dia_siguiente_mes - timedelta(days=primer_dia_siguiente_mes.day)
    # Obtener el número de día del último día del mes
    num_dias = ultimo_dia_mes.day
    return num_dias

# Crear carpetas y archivo

def crear_archivo(ruta_archivo):
    # Obtener el directorio de la ruta del archivo
    directorio = os.path.dirname(ruta_archivo)
    
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Crear el archivo si no existe
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'w') as archivo:
            pass  # No se escribe nada, solo se crea el archivo vacío

crear_archivo(PATH_ARCHIVO)
print(f"El archivo '{PATH_ARCHIVO}' ha sido creado.")

# Crear csv con el header
with open(PATH_ARCHIVO, 'w') as file:
    file.write('|'.join(COLUMNAS_TABLA) + '\n')

# Empezar a generar los registros
for anio in range(2):
    for mes in range(12):
        # Cantidad maxima de dias en el mes
        max_dias = obtener_dias_mes(mes+1, anio+2020)
        for dia in range(max_dias):
            for hora in range(24):
                for minuto in range(60):
                    
                    for segundo in range(60):
                        fecha = datetime(year=anio+ANIO_INICIO, month=mes+MES_INICIO, day=dia+DIA_INICIO, hour=hora, minute=minuto, second=segundo)
                        
                        print("Generando registros para el día: ", fecha)

                        # Para cada segundo del día, generar un registro para cada dispositivo
                        registros = [generar_registro(id_dispositivo, fecha) for id_dispositivo in range(CANT_DISPOSITIVOS_IOT)]
                        
                        print("Escribiendo registros en el archivo")
                        # Escribir un lote de registros en el archivo
                        with open(PATH_ARCHIVO, 'a') as file:
                            file.writelines(registros)
                        
                        # print("Registros escritos en el archivo")
                    

print("FIN")