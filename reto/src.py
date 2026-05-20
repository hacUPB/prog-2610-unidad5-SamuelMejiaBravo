import os
import json
from text_processor import count_words_chars, replace_word, vowel_histogram
from csv_processor import mostrar_primeros_15, calcular_estadisticas, graficar_columna
from json_processor import read_json, create_json, edit_json
from cache_del import limpiar_cache

def cache():
    limpiar_cache()

def list_files():
    path = input("Enter path (or press enter for current): ").strip()
    if not path:
        path = '.'
    try:
        files = os.listdir(path)
        for f in files:
            print(f)
    except FileNotFoundError:
        print("Invalid path.")

def submenu_txt(file_path):
    while True:
        print("\nSubmenú para archivos de texto (.txt)")
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de ocurrencia de las vocales")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            try:
                num_words, chars_with, chars_without = count_words_chars(file_path)
                print(f"Número de palabras: {num_words}")
                print(f"Número de caracteres (con espacios): {chars_with}")
                print(f"Número de caracteres (sin espacios): {chars_without}")
            except FileNotFoundError:
                print("Archivo no encontrado.")
        elif opcion == '2':
            old_word = input("Palabra a buscar: ")
            new_word = input("Palabra por la que reemplazar: ")
            try:
                replace_word(file_path, old_word, new_word)
            except FileNotFoundError:
                print("Archivo no encontrado.")
        elif opcion == '3':
            try:
                vowel_histogram(file_path)
            except FileNotFoundError:
                print("Archivo no encontrado.")
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

def submenu_csv(file_path):
    while True:
        print("Elija la opción de separador:")
        print("1. Coma (,)")
        print("2. Punto y coma (;)")
        print("3. Otro (ingresar el separador manualmente)")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            separador = ','
            break
        elif opcion == '2':
            separador = ';'
            break
        elif opcion == '3':
            separador = input("Ingresa el separador: ")
            break
        else:
            print("Opción inválida.")

    while True:
        print("\nSubmenú para archivos .csv")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular Estadísticas")
        print("3. Graficar una columna completa con los datos")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            try:
                mostrar_primeros_15(file_path, separador)
            except FileNotFoundError:
                print("Archivo no encontrado.")
        elif opcion == '2':
            col = input("Nombre de la columna: ")
            try:
                stats = calcular_estadisticas(file_path, col, separador)
                if stats:
                    print(f"Número de datos: {stats[0]}")
                    print(f"Promedio: {stats[1]}")
                    print(f"Mediana: {stats[2]}")
                    print(f"Moda: {stats[3]}")
                    print(f"Desviación estándar: {stats[4]}")
                    print(f"Valor máximo: {stats[5]}")
                    print(f"Valor mínimo: {stats[6]}")
            except FileNotFoundError:
                print("Archivo no encontrado.")
        elif opcion == '3':
            col = input("Nombre de la columna: ")
            try:
                graficar_columna(file_path, col, separador)
            except FileNotFoundError:
                print("Archivo no encontrado.")
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

def submenu_json(file_path):
    while True:
        print("\nSubmenú para archivos JSON (.json)")
        print("1. Leer JSON")
        print("2. Editar JSON")
        print("3. Crear nuevo JSON")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            read_json(file_path)
        elif opcion == '2':
            edit_json(file_path)
        elif opcion == '3':
            new_path = input("Ingresa la ruta del nuevo archivo JSON: ")
            create_json(new_path)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

def main():
    while True:
        print("\n### **Menú Principal**")
        print("1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Procesar archivo JSON (.json)")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            list_files()
        elif opcion == '2':
            file_path = input("Ingresa la ruta del archivo .txt: ")
            submenu_txt(file_path)
        elif opcion == '3':
            file_path = input("Ingresa la ruta del archivo .csv: ")
            submenu_csv(file_path)
        elif opcion == '4':
            file_path = input("Ingresa la ruta del archivo .json: ")
            submenu_json(file_path)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

while True:
    try:
        cache()
        break
    except:
        pass

if __name__ == "__main__":
    main()