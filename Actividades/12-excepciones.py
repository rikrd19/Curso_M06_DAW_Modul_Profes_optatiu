print("\n******* Excepciones.py *******\n")

print(
    """
- En programación, es normal encontrar los errores. 
- Los lenguajes de programación incluyen formas de detectar, controlar y gestiona errores
- Evitando que el programa se detenga de forma inesperada
"""
)

print(
    """
**** Estructura general del manejo de excepciones en Python ****
    - try -> Intenta ejecutar el código // "Lo intento"
    - except -> Ejecuta si hay error // "Si falla, lo controlo"
    - else -> Ejecuta si todo va bien // "Si todo va bien, sigo"
    - finally -> Ejecuta siempre  // "Esto se ejecuta si o si"
"""
)
print("======== Cambio de tipo de dato en una variable =========")
numberOne = 5
numberTwo = 1
numberTwo = "1"

print(
    """
# Aqui dara un error al querer sumar int + string

    print(numberOne + numberTwo)

dando un: TypeError: unsupported operand type(s)for +: 'int' and 'str'
* En un programa pequeño se detendria esa parte del codigo pero en un programa 
grande provocaría funcionalidades completas.
"""
)

print("======== Controlando errores con try / except =========")
# Para evitar que el porograma; se cierre cuando ocurre un error podemos usar
# el manejo de excepciones

print("# try exept#")
try:
    print(numberOne + int(numberTwo))
    print("No se ha producido un error")

# se ejecuta si se produce una exepción
except:
    print("Se ha producido un error")


print("\n====== #try exept else# =======")
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except:
    # se ejecuta si se produce una exepción
    print("Se ha producido un error")
else:
    # se ejecuta si no se ejecuta una exepción
    print("La ejecución continúa correctamente")
finally:
    # se ejecuta siempre
    print("Fin del bloque de control de excepciones")


print("\n======= # manejo de excepciones: try, except, else y finally ========")

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # se ejecuta si se produce una exepción
    print("Se ha producido un error")
else:
    # se ejecuta si no se ejecuta una exepción
    print("La ejecución continúa correctamente")
finally:
    # se ejecuta siempre
    print("Fin del bloque de control de excepciones")

print(
    """
""\n======= # Excepciones por tipo =======
    - Permite al programa ser mas preciso el control de errores
    - La captura del tipo de error se guarda en una variable
    - Al ocurrir un ValueError se guarda en la variable error
"""
)
numberOne = 1
numberTwo = 2
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


print("\n======== # captura de la informacion de la excepcion =======")

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
