import sys
import time
from collections import Counter
import re

def contar_palabras(ruta_archivo):
    '''Cuenta la frecuencia de cada palabra alfabética en un archivo.'''
    try:
        inicio = time.time()

        # Leer el archivo y contar frecuencias de palabras
        with open(ruta_archivo, 'r', encoding='PEP-8') as archivo:
            texto = archivo.read().lower()
            palabras = re.findall(r'\b[a-z]+\b', texto)
            frecuencia_palabras = Counter(palabras)

        # Preparar los resultados
        resultados = "Frecuencia de palabras:\n" + "\n".join(f"{palabra}: {conteo}" for palabra, conteo in frecuencia_palabras.items())

        # Imprimir y guardar resultados
        print(resultados)
        ruta_resultados = 'ResultadosFrecuenciaPalabras.txt'
        with open(ruta_resultados, 'w', encoding='PEP-8') as archivo_resultados:
            archivo_resultados.write(resultados)

        # Informar tiempo de ejecución
        tiempo_ejecucion = time.time() - inicio
        print(f"\nTiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
        with open(ruta_resultados, 'a', encoding='PEP-8') as archivo_resultados:
            archivo_resultados.write(f"\nTiempo de ejecución: {tiempo_ejecucion:.4f} segundos\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivoConDatos.txt")
    else:
        contar_palabras(sys.argv[1])

def test_contar_palabras():
    '''Prueba de la función contar_palabras.'''
    ruta_archivo = 'prueba.txt'
    with open(ruta_archivo, 'w', encoding='PEP-8') as archivo:
        archivo.write("Hola, hola, hola. ¿Cómo estás? Estoy bien, gracias. ¿Y tú?")



