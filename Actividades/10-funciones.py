print("\n" + "=" * 50)
print(
    """
*******  FUNCIONES EN PYTHON *******
"""
)
print("=" * 50)


print(
    """
* Una función es un bloque de código que se puede 
reutilizar para realizar una tarea específica
** Permite organizar el programa, evitar repetir código y 
facilitar el mantenimiento.
*** Esto permite no rescribir el mismo código muchas veces, 
sino llamarlo cuando se necesite.
**** La función se define con la palabra reservada 'def' 
seguida del nombre de la función.
"""
)
print("-" * 50)


def my_function():
    print("Esto es una función")


my_function()

print("-" * 50)
print(
    """
--- Ventaja principal de las funciones ---
* Centraliza una operación en un solo lugar:
    + conectarse a un servidor
    + descargar una base de datos
    + Procesar información 
    + Guardar resultados
    + para ejecutar una operación se llama la función
** Se evita:
    + cometer más errores
    + tardar mas tiempo en programar
    + dificultad de manterner el código
"""
)


def my_functions():
    print("Esto es una función")


my_functions()
my_functions()
my_functions()

print("-" * 60)
print("** Permite ejecutar la misma operación con distintos valores")


def sum_two_values(first_number, second_number):
    print(first_number + second_number)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values(1.4, 5.2)  # tipo float #

print("-" * 60)
print(
    """ 
** Si se declara los valores numéricos como strings así serán considerados
no realizándose las operaciones Python las acepta y la respuesta será un string.
"""
)


def sum_twos_values(first_number: int, second_number: int):
    print(first_number + second_number)

# se declaron int pero se colocan valores Strings no realizandose la operacion
sum_twos_values("5", "7")

print("-" * 60)
print(
    """ 
----  Funciones con 'return'  ----
* el resultado se devuelve usando la palabra clave 'return'
** la diferencia con 'print', 'return' no muestra el resultado en pantalla 
*** el valor lo devuelve para usarse mas adelante en el programa
"""
)


def sum_two_values_with_return(firsts_value, second_value):
    return firsts_value + second_value


print("El resultado de la suma es: ", sum_two_values_with_return(10, 5))


print("-" * 60)
print("---- Guardar el valor devuelto por una función  ----")

my_result = sum_two_values_with_return(10, 5)
print("El resultado de la suma es: ", my_result)


print("-" * 60)
print(
    """ 
----  Función con varios parámetros y f-strings  ----
* dentro de la función se usa el format 'f-string' para unir ambos valores en una sola
cadena de texto y mostrarlos en pantalla.
"""
)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name("Lopez", "Geral")

print("-" * 60)
print(
    """ 
----  ¿Qué ocurre en este caso?  ----
* Llamando a la función usando 'argumentos con nombre'
** se explican explicitamente que valor corresponde a cada parámetro
"""
)


def prin_name(name, surname):
    print(f"{name} {surname}")


prin_name(surname="Lopez", name="Geral")


print("-" * 60)
print(
    """ 
----  Parámetros con valor por defecto  ----
* Un parámetro con valor por defecto se le asigna un valor 
directamente en la definición de la función
** si al llamar la función no se envia ese parámetro, Python 
utiliza automáticamente el valor por defecto
*** estos valores permiten llamar a una función sin necesidad
de enviar todos los argumentos
"""
)


print("-" * 60)
print(
    """ 
----  Parámetros variables con *args  ----
*args es una forma de definir una función que puede recibir
un número variable de argumentos.

** estos valores se almacenan en una tupla, permitiendo trabajar con 
muchos parámetros sin saber cuántos se van a recibir
"""
)


print("-" * 60)
print(
    """ 
----  ¿Qué significa *text?  ----
- El símbolo * indica que la función puede recibir 'un número variable de argumentos'
- todos los valores enviados se almacenan dentro de una tupla llamado text
"""
)


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Geral", "Lopez")


print("-" * 60)
print(
    """ 
----  Uso de *args con procesamiento de datos  ----
- La función recibe número variable de textos usando *tests
- Cada texto se procesa dentro del bucle FOR y se convierte 
a mayúsculas usando el método .upper()
"""
)


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "Profesgeralv")
print_upper_texts("Hola")
