print("\n********** Modulos ************\n")

print("""
¿Qué es un módulo?
------------------
- Forma de organizar código propio o externo
- Al crecer un programa se tiene que hacer claro, mantenible y escalable
- Siendo la idea principal poder importar los archivos en otros programas
- Se evita repetir código y facilitar el desarrollo de aplicaciones a mas grande

* Si se quiere reutilizar código de un archivo en otro, con 'def' se define la función
""")
def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()    


print("""
** Al copiar el código y llevarse a un nuevo archivo al intentar llamar a la 
    función directamente sin importarla, el programa dará 'error' al no reconocerla
""")
# modules#de  my_function():
my_function() #x Error: name 'my_function' is not defined

print("""
*** Recordar: que en my_function se tenia una función sencilla 
    sumar dos valores recibidos como parámetros
""")
def sum_two_values(first_number, second_number):
    print(first_number + second_number)
print("""
- Si se necesitare en otro archivo, la solución instintiva es copiar y pegar
- Produciendo el error más típico en programación
""")
# modules#de my_function():
def sum_two_values(first_number, second_number):
    print(first_number + second_number)

print("""
- y se llama facilmente sum: values(5, 3) y se tiene valores dando = 8
""")
# modules#de my_function():
def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 3)

print("""
- Esto da resultado 8, la solución no correcta. Si la función cambia se tiene
    en el futuro se tendría que actualizar en todos los archivos donde se copió.
- Solución es usar módulos: en lugar de copiar se debe 'importar' desde el archivo original.
- Al ser copiada en varios archivos se generan duplicación de código
- Al descubrir un error de lógica se tendría que modificar la función en cada archivo donde se colocó
- La solución: módulos en lugar de copiar la función se debe guardar en un archivo separado
- En los archivos que se necesiten se importan usando la palabra reservada import

    import 10_functions   # fallará: porque los modulos empiecen con números
    
    sum_two_values(5, 3)
    
- Se crea un fichero llamado module.py   
""")

def sum(numberOne, numberTwo, numberThree):
    print(numberOne + numberTwo + numberThree)

# A continuación se sustituye el contenido del fichero, por:

def sum(numberOne, numberTwo, numberThree):
    print(numberOne + numberTwo + numberThree)

print(
    """
- Se sustituye el contenido del fichero y al ejecutar ya no se produce error
#modules#de my_function():

import module
module.sum(5, 3, 1)

my_module.printValue("Hola Python")
""")

print("** Al importar una función de un módulo se usa la palabra clave 'from' ")
from my_module import sum
sum (1,2,3)

print("** O se puede importar por separado **")
from my_module import sum, printValue

sum(1, 2, 3)
print("hola python")

print("""
** Uso del modulo Math
------------------------
    - En Python existen integrados que ya contienen funciones y constantes listas 
    para usar, como el módulo math.
    - La Expresión math.pi representa el valor del número 'pi'. Al utilizar 
    print(math.pi), mostramos su valor en pantalla.
    - Al usar math.pow(2, 8) permite calcular una potencia -> 2 elevado a la 8
""")
import math

math.pi
print(math.pi)
print(math.pow(2, 8))

from math import pi
print(pi)

print("""\n
### importacion con alias ###\n
    - También se puede importar un elemento de un módulo y asignarle un nombre
    diferente utilizando la palabra clave 'as' -> llamado 'alias'
    
    ** Ejemplo: 
        se importa la constante pi del módulo math y le damos el nombre  PI_VALUE: 
# """)

from math import pi as PI_VALUE
print(PI_VALUE)
