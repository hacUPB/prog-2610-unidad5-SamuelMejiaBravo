import csv
import statistics
import matplotlib.pyplot as plt


def mostrar_primeros_15(ruta_archivo, separador=','):
    try:
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as f:
            lector = csv.reader(f, delimiter=separador)
            encabezados = next(lector, None)
            if encabezados:
                encabezados = [h.strip() for h in encabezados]
                print(','.join(encabezados))
            for i, fila in enumerate(lector):
                if i >= 15:
                    break
                print(','.join(fila))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except StopIteration:
        print("Archivo CSV vacío.")


def calcular_estadisticas(ruta_archivo, columna, separador=','):
    try:
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as f:
            lector = csv.reader(f, delimiter=separador)
            encabezados = next(lector, None)
            if encabezados:
                encabezados = [h.strip() for h in encabezados]
            columna = columna.strip()
            if not encabezados or columna not in encabezados:
                print("Columna no encontrada.")
                return None
            indice_columna = encabezados.index(columna)
            datos = []
            for fila in lector:
                if len(fila) > indice_columna:
                    try:
                        valor = float(fila[indice_columna].strip())
                        datos.append(valor)
                    except ValueError:
                        pass  # saltear no numéricos
            if not datos:
                print("No hay datos numéricos en la columna.")
                return None
            num_datos = len(datos)
            media = sum(datos) / num_datos
            datos_ordenados = sorted(datos)
            mediana = datos_ordenados[num_datos // 2] if num_datos % 2 == 1 else (datos_ordenados[num_datos // 2 - 1] + datos_ordenados[num_datos // 2]) / 2
            try:
                moda = statistics.mode(datos)
            except statistics.StatisticsError:
                moda = None  # No hay moda única
            varianza = sum((x - media) ** 2 for x in datos) / num_datos
            desv_est = varianza ** 0.5
            valor_max = max(datos)
            valor_min = min(datos)
            return num_datos, media, mediana, moda, desv_est, valor_max, valor_min
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None


def graficar_columna(ruta_archivo, columna, separador=','):
    try:
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as f:
            lector = csv.reader(f, delimiter=separador)
            encabezados = next(lector, None)
            if encabezados:
                encabezados = [h.strip() for h in encabezados]
            columna = columna.strip()
            if not encabezados or columna not in encabezados:
                print("Columna no encontrada.")
                return
            indice_columna = encabezados.index(columna)
            datos = []
            for fila in lector:
                if len(fila) > indice_columna:
                    try:
                        valor = float(fila[indice_columna].strip())
                        datos.append(valor)
                    except ValueError:
                        pass
            if not datos:
                print("No hay datos numéricos en la columna.")
                return

            # Gráfica de dispersión
            plt.figure(figsize=(10, 5))
            plt.scatter(range(len(datos)), datos, color='blue', alpha=0.7)
            plt.title(f'Gráfica de dispersión: {columna}')
            plt.xlabel('Índice')
            plt.ylabel(columna)
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.tight_layout()
            plt.show()

            # Gráfico de barras con datos ordenados: clasificar valores y mostrar los 10 principales
            datos_ordenados = sorted(datos, reverse=True)
            datos_barras = datos_ordenados[:10] if len(datos_ordenados) >= 10 else datos_ordenados
            plt.figure(figsize=(10, 5))
            plt.bar(range(len(datos_barras)), datos_barras, color='orange', edgecolor='black')
            plt.title(f'Gráfico de barras (valores ordenados) de {columna}')
            plt.xlabel('Posición')
            plt.ylabel(columna)
            plt.xticks(range(len(datos_barras)), [str(i + 1) for i in range(len(datos_barras))])
            plt.tight_layout()
            plt.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")