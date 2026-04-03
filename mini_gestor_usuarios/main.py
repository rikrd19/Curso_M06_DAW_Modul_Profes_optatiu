"""
Programa principal: menú interactivo y lista de usuarios.
Aquí se aplica el control de errores con try / except / else / finally.
"""

from usuario import Usuario

from utils import (
    mostrar_usuarios_numerados,
    pedir_email,
    pedir_edad_texto,
    pedir_indice,
    pedir_nombre,
)


def crear_usuario(usuarios):
    """
    Crea un usuario y lo añade a la lista.
    try: intentamos leer datos, convertir edad y construir Usuario (validación en setters).
    except ValueError: datos incorrectos (edad no numérica, validaciones de la clase).
    except Exception: cualquier otro error inesperado.
    else: solo si no hubo excepción (usuario creado bien).
    finally: se ejecuta siempre (mensaje de cierre de la operación).
    """
    print("\n--- Crear usuario ---")
    try:
        nombre = pedir_nombre()
        edad_texto = pedir_edad_texto()
        try:
            edad = int(edad_texto)
        except ValueError:
            raise ValueError("La edad debe ser un número entero válido.")

        email = pedir_email()

        nuevo = Usuario(nombre, edad, email)
        usuarios.append(nuevo)

    except ValueError as error:
        # Errores de validación (int() fallido o mensajes de los setters de Usuario)
        print(f"Error de validación: {error}")

    except Exception as error:
        # Cualquier otro error no previsto
        print(f"Error inesperado: {error}")

    else:
        print("Usuario creado correctamente.")

    finally:
        print("Operación de creación finalizada.\n")


def modificar_email(usuarios):
    print("\n--- Modificar email ---")
    if not usuarios:
        print("No hay usuarios. Crea uno antes.\n")
        return

    mostrar_usuarios_numerados(usuarios)
    indice = pedir_indice(len(usuarios))
    if indice is None:
        return

    nuevo_email = input("Nuevo email: ").strip()
    try:
        usuarios[indice].set_email(nuevo_email)
    except ValueError as error:
        print(f"Error de validación: {error}")
    else:
        print("Email actualizado correctamente.")
    print()


def menu():
    usuarios = []

    while True:
        print("=== Gestor de usuarios ===")
        print("1. Crear usuario")
        print("2. Mostrar usuarios")
        print("3. Modificar email de un usuario")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            crear_usuario(usuarios)
        elif opcion == "2":
            print("\n--- Lista de usuarios ---")
            mostrar_usuarios_numerados(usuarios)
            print()
        elif opcion == "3":
            modificar_email(usuarios)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Elige 1, 2, 3 o 4.\n")


if __name__ == "__main__":
    menu()
