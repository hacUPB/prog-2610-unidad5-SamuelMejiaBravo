import csv

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
            # Simple text scatter: print indices and values (limited to first 20)
            print("Gráfico de dispersión (índice, valor):")
            for i, val in enumerate(data[:20]):
                print(f"{i}: {val}")
            if len(data) > 20:
                print("... (mostrando solo los primeros 20)")
            # Text-based histogram
            min_val = min(data)
            max_val = max(data)
            if min_val == max_val:
                print("Todos los valores son iguales, no se puede crear histograma.")
                return
            bins = 10
            bin_width = (max_val - min_val) / bins
            hist = [0] * bins
            for val in data:
                bin_idx = int((val - min_val) / bin_width)
                if bin_idx == bins:
                    bin_idx -= 1
                hist[bin_idx] += 1
            print("Histograma:")
            for i in range(bins):
                bin_start = min_val + i * bin_width
                bin_end = min_val + (i + 1) * bin_width
                print(f"{bin_start:.2f}-{bin_end:.2f}: {'*' * hist[i]}")
    except FileNotFoundError:
        print("Archivo no encontrado.")