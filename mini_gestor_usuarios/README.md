# Mini gestor de usuarios (Python)

Aplicación de consola para gestionar usuarios de una plataforma interna. Implementa **programación orientada a objetos**, **encapsulación** con atributos privados, **getters y setters con validación**, y **manejo de excepciones** (`try` / `except` / `else` / `finally`).

## Requisitos

- Python 3 instalado (recomendado 3.10 o superior).

## Estructura del proyecto

| Archivo      | Descripción |
|-------------|-------------|
| `main.py`   | Menú principal, lista de usuarios y flujo con excepciones obligatorias al crear usuario. |
| `usuario.py`| Clase `Usuario` con atributos privados, getters, setters y método `__str__`. |
| `utils.py`  | Funciones auxiliares: pedir datos por consola y mostrar usuarios numerados. |

## Cómo ejecutar

Desde esta carpeta (`mini_gestor_usuarios`):

```bash
python3 main.py
```

En Windows, si `python3` no existe:

```bash
python main.py
```

## Funcionalidades (menú)

1. **Crear usuario** — Pide nombre, edad y email; valida datos y añade el usuario a una lista en memoria.
2. **Mostrar usuarios** — Lista numerada `[0]`, `[1]`, … para identificar cada usuario.
3. **Modificar email** — Elige usuario por índice y actualiza el email usando el setter (con validación).
4. **Salir** — Cierra el programa.

## Validaciones

- **Nombre:** no puede estar vacío ni ser solo espacios.
- **Edad:** número entero mayor que 0.
- **Email:** debe contener al menos `@` y `.` (validación simple según el enunciado).

Si un dato no es válido, se lanza `ValueError` con un mensaje claro y el programa **no se rompe**; se informa al usuario y se vuelve al menú.

## Conceptos implementados 

- **Encapsulación:** los datos (`__nombre`, `__edad`, `__email`) son privados; solo se accede mediante getters y setters.
- **Setters con reglas:** centralizan la validación; si falla, `raise ValueError(...)`.
- **`__str__`:** define la representación en texto del objeto (lo que se ve al imprimir un `Usuario`).
- **Excepciones en `main.py`:** al crear usuario se usa `try`, `except ValueError`, `except Exception`, `else` y `finally` para cumplir el enunciado y diferenciar errores de validación de errores inesperados.

## Autor

Proyecto individual realizado por Ricardo Avila B. — módulo DAW Optativa (Programación en Python).
