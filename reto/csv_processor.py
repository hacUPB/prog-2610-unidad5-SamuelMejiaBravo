import csv
import matplotlib.pyplot as plt


def show_first_15(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if headers:
                print(','.join(headers))
            for i, row in enumerate(reader):
                if i >= 15:
                    break
                print(','.join(row))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except StopIteration:
        print("Archivo CSV vacío.")


def calculate_stats(file_path, column):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if not headers or column not in headers:
                print("Columna no encontrada.")
                return None
            col_index = headers.index(column)
            data = []
            for row in reader:
                if len(row) > col_index:
                    try:
                        val = float(row[col_index])
                        data.append(val)
                    except ValueError:
                        pass  # skip non-numeric
            if not data:
                print("No hay datos numéricos en la columna.")
                return None
            num_data = len(data)
            mean = sum(data) / num_data
            data_sorted = sorted(data)
            median = data_sorted[num_data // 2] if num_data % 2 == 1 else (data_sorted[num_data // 2 - 1] + data_sorted[num_data // 2]) / 2
            variance = sum((x - mean) ** 2 for x in data) / num_data
            std = variance ** 0.5
            max_val = max(data)
            min_val = min(data)
            return num_data, mean, median, std, max_val, min_val
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None


def plot_column(file_path, column):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if not headers or column not in headers:
                print("Columna no encontrada.")
                return
            col_index = headers.index(column)
            data = []
            for row in reader:
                if len(row) > col_index:
                    try:
                        val = float(row[col_index])
                        data.append(val)
                    except ValueError:
                        pass
            if not data:
                print("No hay datos numéricos en la columna.")
                return

            # Scatter plot
            plt.figure(figsize=(10, 5))
            plt.scatter(range(len(data)), data, color='blue', alpha=0.7)
            plt.title(f'Gráfica de dispersión: {column}')
            plt.xlabel('Índice')
            plt.ylabel(column)
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.tight_layout()
            plt.show()

            # Bar plot for rearranged data: sort values and display top 10
            sorted_data = sorted(data, reverse=True)
            bar_data = sorted_data[:10] if len(sorted_data) >= 10 else sorted_data
            plt.figure(figsize=(10, 5))
            plt.bar(range(len(bar_data)), bar_data, color='orange', edgecolor='black')
            plt.title(f'Gráfico de barras (valores ordenados) de {column}')
            plt.xlabel('Posición')
            plt.ylabel(column)
            plt.xticks(range(len(bar_data)), [str(i + 1) for i in range(len(bar_data))])
            plt.tight_layout()
            plt.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")