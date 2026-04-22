import json

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar JSON.")

def create_json(file_path):
    data = {}
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print("Archivo JSON creado vacío.")
    except Exception as e:
        print(f"Error al crear archivo: {e}")

def edit_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return
    except json.JSONDecodeError:
        print("JSON inválido.")
        return

    while True:
        print("\nDatos actuales:")
        print(json.dumps(data, indent=4))
        print("\nOpciones de edición:")
        print("1. Agregar/Modificar clave")
        print("2. Eliminar clave")
        print("3. Guardar y salir")
        choice = input("Elige una opción: ")
        if choice == '1':
            key = input("Ingresa la clave: ")
            value_str = input("Ingresa el valor (ej: 'string', 123, [1,2], {'key':'val'}): ")
            try:
                value = eval(value_str)
                data[key] = value
                print("Clave agregada/modificada.")
            except Exception as e:
                print(f"Valor inválido: {e}")
        elif choice == '2':
            key = input("Ingresa la clave a eliminar: ")
            if key in data:
                del data[key]
                print("Clave eliminada.")
            else:
                print("Clave no encontrada.")
        elif choice == '3':
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                print("Cambios guardados.")
                break
            except Exception as e:
                print(f"Error al guardar: {e}")
        else:
            print("Opción inválida.")