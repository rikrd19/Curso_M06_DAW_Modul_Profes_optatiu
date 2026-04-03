"""
Clase Usuario: modelo de un usuario de la plataforma.
Encapsulación: los datos sensibles solo se leen o cambian con getters y setters.
"""


class Usuario:
    """
    Representa un usuario con nombre, edad y email.
    Los atributos son privados (__nombre, __edad, __email) para que no se
    modifiquen desde fuera sin pasar por la validación de los setters.
    """

    def __init__(self, nombre, edad, email):
    # Se usan los setters para validar desde el primer momento
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_email(email)

    # --- Getters: solo lectura controlada de los atributos privados ---
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_email(self):
        return self.__email

    # --- Setters: escritura con reglas; si fallan, ValueError con mensaje claro ---
    def set_nombre(self, nombre):
        if nombre is None or str(nombre).strip() == "":
            raise ValueError("El nombre no puede estar vacío ni ser solo espacios.")
        self.__nombre = str(nombre).strip()

    def set_edad(self, edad):
        if not isinstance(edad, int):
            raise ValueError("La edad debe ser un número entero mayor que 0.")
        if edad <= 0:
            raise ValueError("La edad debe ser un número entero mayor que 0.")
        self.__edad = edad

    def set_email(self, email):
        if email is None:
            raise ValueError("Email inválido: debe contener @ y .")
        correo = str(email).strip()
        if "@" not in correo or "." not in correo:
            raise ValueError("Email inválido: debe contener @ y .")
        self.__email = correo

    def __str__(self):
        """
        Método especial: al hacer print(usuario) o str(usuario), Python usa __str__.
        Devuelve un texto legible con los datos del usuario (sin exponer cómo
        están guardados internamente).
        """
        return (
            f"Usuario: {self.__nombre} | Edad: {self.__edad} | Email: {self.__email}"
        )
