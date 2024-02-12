import json
import sys
import time

def cargar_archivo_json(ruta_archivo):
    """Carga los datos de un archivo JSON."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError as e:
        print(f"Error: No se encontró el archivo {ruta_archivo}.")
    except json.JSONDecodeError as e:
        print(f"Error: No se pudo decodificar el JSON en {ruta_archivo}.")
    return None

def calcular_costo_total(catalogo_precios, registros_ventas):
    """Calcula el costo total basado en los registros de ventas y el catálogo de precios."""
    total_costo = sum(
        venta['Quantity'] * next(
            (producto['price'] for producto in catalogo_precios if producto['title'] == venta.get('Product', '')),
            0
        )
        for venta in registros_ventas
    )
    return total_costo

def main():
    """Función principal del programa."""
    if len(sys.argv) != 3:
        print("Uso: python nombre_programa.py TC1.ProductList.json TC2.Sales.json")
        sys.exit(1)

    ruta_catalogo_precios = sys.argv[1]
    ruta_registros_ventas = sys.argv[2]

    catalogo_precios = cargar_archivo_json(ruta_catalogo_precios)
    registros_ventas = cargar_archivo_json(ruta_registros_ventas)

    if catalogo_precios is None or registros_ventas is None:
        sys.exit(1)

    tiempo_inicio = time.time()

    costo_total = calcular_costo_total(catalogo_precios, registros_ventas)

    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    print(f"Costo Total: ${costo_total:.2f}")
    print(f"Tiempo Transcurrido: {tiempo_transcurrido:.4f} segundos")

    with open('ResultadosVentas.txt', 'w', encoding='utf-8') as archivo_resultados:
        archivo_resultados.write(f"Costo Total: ${costo_total:.2f}\n")
        archivo_resultados.write(f"Tiempo Transcurrido: {tiempo_transcurrido:.4f} segundos\n")

if __name__ == "__main__":
    main()
