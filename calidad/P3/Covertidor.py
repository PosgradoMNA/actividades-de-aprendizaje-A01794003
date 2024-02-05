import time
import sys
from collections import Counter
import re

def convertir_numeros(ruta_archivo):
    try:
        with open(ruta_archivo,'r') as archivo:
            # Conversión directa de cada línea a int y filtrado de líneas vacías o no numéricas
            numeros = [int(linea.strip()) for linea in archivo if linea.strip().isdigit()]
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
        return
    except ValueError:
        print(f"Error al leer el archivo: {ruta_archivo} contiene datos no válidos.")
        return

    start_time = time.time()

    # Comprensión de listas para generar resultados binarios y hexadecimales
    resultados_binarios = [bin(num)[2:] for num in numeros]
    resultados_hexadecimales = [hex(num)[2:] for num in numeros]

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Función para imprimir y guardar resultados
    imprimir_y_guardar_resultados(resultados_binarios, resultados_hexadecimales, elapsed_time)

def imprimir_y_guardar_resultados(binarios, hexadecimales, tiempo):
    print("Resultados en binario:")
    print('\n'.join(binarios))
    print("\nResultados en hexadecimal:")
    print('\n'.join(hexadecimales))
    print(f"\nTiempo transcurrido: {tiempo:.4f} segundos")

    # Ajusta la ruta de salida según tus necesidades
    ruta_salida = 'Resultados_Conversion.txt'
    with open(ruta_salida, 'w') as archivo_resultados:
        archivo_resultados.write("Resultados en binario:\n")
        archivo_resultados.write('\n'.join(binarios) + '\n\n')
        archivo_resultados.write("Resultados en hexadecimal:\n")
        archivo_resultados.write('\n'.join(hexadecimales) + '\n')
        archivo_resultados.write(f"\nTiempo transcurrido: {tiempo:.4f} segundos\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
    else:
        convertir_numeros(sys.argv[1])