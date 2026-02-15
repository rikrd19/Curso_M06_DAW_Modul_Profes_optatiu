print("\n" + "=" * 50)
print(
    """
    *******  CLASES  *******
"""
)
print("=" * 50)


print("-" * 60)
print(
    """ 
* En programación, una clase es una estructura que nos permite 
definir un objeto desde su creación hasta su uso.
    + Clase: molde para crear objetos
    + Atributos: Características/propiedades
    + Métodos: acciones que puede hacer

** Las clases permiten: 
    + organizar el código 
    + Facilitar su comprensión
    + Reutilizarlo en diferentes partes del programa

*** Las clases pueden contener:
    + Atributos: describen las propiedades del objeto
    + Métodos: describen las acciones que el objeto puede realizar.
"""
)

print("-" * 60)
print(
    """ 
* las clases se deben definir con instrucciones en su interior 
para que no de error de sintaxis

class MyEmptyPerson:  # Error de sintaxis

** El uso de la instrucción 'pass' indica que la clase existe 
pero que no tiene contenido
"""
)

class MyEmptyPerson:
    pass 


print("-" * 60)
print(
    """ 
* Los nombres de las variables, funciones y métodos se usa 
la escritura de estilo 'snake_case'.
** Pero para los nombres de clases se usa CamelCase o PascalCase
*** Esto mejora la buena practica de programación, mejora la lectura y comprensión 
del código.
"""
)
print(MyEmptyPerson) # Muestra la definición de la clase (el molde)
print("-" * 60)

print(MyEmptyPerson()) # crea un objeto (instancia) a partir de dicha clase


print("-" * 60)
print(
    """ 
* Uso del constructor
METODO __init__ funciona como un constructor que se ejecuta automáticamente cada vez
que se crea un nuevo objeto de una clase. Función principal "inicializar los atributos" 
y preparar la estructura interna del objeto desde el principio.
    - las clases pueden existir vacias (usando pass).
    - se hace la referencia a la clase como definición "sin paréntesis", pero se 
    generan objetos (instancias) utilizandolos con paréntesis.
"""
)

class Person:
    def __init__(self,name, surname):
        pass


print("-" * 60)
print(
    """ 
** Uso de self y asignacino de atributos
    + al usar self se trabaja directamente con la instancia del objeto
        que se está creando.
    + 'self' hace referencia al propio objeto.
    + los objetos se acceden mediante la notación punto (.)
"""
)

class Persona:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


print("-" * 60)
print("***** CREACION DEL OBJETO ******\n")

my_person = Persona("Geral", "Lopez")
print(
    f"{my_person.name} {my_person.surname}"  # aqui el objeto my_person almacena internamente los valores
)


print("-" * 60)
print("""
***** Tipo de datos en los atributos ******\n
    + a los atributos se les puede asignar cualquier tipo de datos:
        - cadenas de texto
        - números
        - listas
        - tuplas
        - diccionarios
"""
)

class Persons:

    def __init__(self, name, surname):
        self.full_name = f"{surname} {surname}"

    def walk(self):
        print(f"{self.full_name} esta caminando")


print("-" * 60)
print(
    """
***** Uso del objeto *****
"""
)

# crear un objeto
my_person = Persons("Geral", "Lopez")

# Mostrar el atributo
print(my_person.full_name)

# Ejecutar el metodo
my_person.walk()


print("-" * 60)
print(
    """
***** Modificacion de un atributo despues de crear el objeto *****\n
+ en Python los atributos de un objeto pueden modificarse directamente 
    desde fuera de la clase
+ en Python: 
    - los atributos son publicos por defecto 
    - pueden modificarse desde fuera 
    - el objeto sigue siendo el mismo, pero cambia su estado
+ NOTA : en Python existe uan estructura base al construir clases: 
    - definir la clase
    - crear el constructor
    - definir atributos
    - definir métodos
"""
)

# crear un objeto
my_person = Persons("Geral", "Lopez")

# acceder al atributo
print(my_person.full_name)

# Ejecutar el metodo
my_person.walk()

# Modificar directamente el atributo
my_person.full_name = "Andrés (El loco de los gatos)"

# Volver a mostrar el atributo
print(my_person.full_name)