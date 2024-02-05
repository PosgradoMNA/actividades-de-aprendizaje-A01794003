import time
import sys
from collections import Counter
import re
from statistics import mean, median, mode, stdev

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return [float(linea.strip()) for linea in archivo]
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    except ValueError:
        print(f"Error: El archivo '{nombre_archivo}' contiene datos no válidos.")
        return None

def calcular_estadisticas(ruta_archivo):
    datos = leer_archivo(r'C:\Users\sisti\Downloads\codigos\P3\TC3.txt')
    if datos is None:
        return

    inicio = time.time()

    resultados = {
        "COUNT": len(datos),
        "MEAN": mean(datos),
        "MEDIAN": median(datos),
        "MODE": mode(datos),
        "SD": stdev(datos),
        "VARIANCE": stdev(datos)**2
    }

    fin = time.time()
    tiempo_transcurrido = fin - inicio

    print_resultados(resultados, tiempo_transcurrido)

def print_resultados(resultados, tiempo_transcurrido):
    print("Estadísticas de los Datos")
    for clave, valor in resultados.items():
        print(f"{clave}: {valor}")
    print(f"Tiempo transcurrido: {tiempo_transcurrido:.4f} segundos")

    with open("ResultadosEstadisticas.txt", 'w') as archivo:
        for clave, valor in resultados.items():
            archivo.write(f"{clave}: {valor}\n")
        archivo.write(f"Tiempo transcurrido: {tiempo_transcurrido:.4f} segundos\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py ")
    else:
        calcular_estadisticas(sys.argv[1])