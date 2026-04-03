"""
Funciones auxiliares: pedir datos por consola y mostrar listas numeradas.
Así el menú principal queda más simple y ordenado.
"""


def pedir_nombre():
    return input("Nombre: ")


def pedir_edad_texto():
    """Devuelve el texto que escribe el usuario; la conversión a int se hace donde convenga."""
    return input("Edad: ").strip()


def pedir_email():
    return input("Email: ").strip()


def mostrar_usuarios_numerados(usuarios):
    """Muestra cada usuario con su índice [0], [1], ... para poder elegir uno."""
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for i, usuario in enumerate(usuarios):
        print(f"[{i}] {usuario}")


def pedir_indice(maximo_exclusivo):
    """
    Pide un índice entero. Devuelve None si no es válido (sin tirar el programa).
    maximo_exclusivo: por ejemplo len(lista), índices válidos 0 .. max-1
    """
    texto = input("Número del usuario (índice): ").strip()
    try:
        indice = int(texto)
    except ValueError:
        print("Debes escribir un número entero para el índice.")
        return None
    if indice < 0 or indice >= maximo_exclusivo:
        print("Ese índice no existe en la lista.")
        return None
    return indice
