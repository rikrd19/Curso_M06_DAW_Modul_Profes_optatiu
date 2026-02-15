print(
    """
***** Los loops o bucles son estructuras que permiten repetir un bloque de
        código varias veces mientras se cumpla una condición o mientras haya
        elementos que recorrer, automatizando la repetición. 
""")

print(" ** Tipo 'while' - repite mientras una condicion sea verdadera **")

# incorrecto --> la condicion nunca cambia, bucle infinito

my_condition = 0
while my_condition < 10:
    print(my_condition) # bycle infinito 
    break # colocado para que rompa el bucle 
print("-"* 40)  

# correcto
while my_condition < 10:
    print(my_condition)
    my_condition += 2

print("\n" + "=" * 50)
print(
    """
** Particularidad de Python: While con else, al
terminar el bucle 'While' se puede usar el bloque 'else'
"""
)
print("=" * 50)

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("mi condicion es mayor o igual que 10")

print("\n" + "=" * 60)
print("""
** Uso de while seguido de if: el bucle while repite el codigo
mientras la condición sea verdadera. Al terminar el bucle el programa
continua con un if que evalúa el valor final de la variable.
""")
print("=" * 60)

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2

if my_condition == 10:
    print("Mi condicion es igual a 10")
else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")


print(
    """
\n**** NOTA: Uso correcto de 'if' y 'elif' y 'else' en bucles: se pueden 
usar sin problemas, pero 'elif' siempre se usa despues de un if y con 
la misma indentación. *****
"""
)


print("\n" + "=" * 60)
print("""
*** Recordatorio sobre el if:  sirve para ejecutar un bloque de código solo
cuando una condicion es verdadera y si es falsa el bloque es ignorado y el
programa continua.
""")
print("=" * 60)

my_condition = 0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
    print(my_condition)


print("\n" + "=" * 60)
print(
    """
*** Detener un bucle while con break: mientras su condición sea verdadera
en ocaciones es necesario detener el bucle antes que la condicion deje de
cumplirse, usando la palabra clave 'break' permitiendo salir del bucle al 
cumplirse una condición específica.
"""
)
print("=" * 60)

while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")


print("\n\n **** Bucle FOR ****")
print("\n" + "=" * 60)
print(
    """
* EL BUCLE FOR permite recorrer los elementos de un set, una 
lista, una tupla o las claves de un diccionario.
** El FOR se ejecutará dependiendo de cuantos elementos tenga 
la colección que esté recorriendo.
*** En cada iteración el bucle toma un elemento de la colección 
y lo guarda en una variable para poder utilizarlo dentro del 
bloque de código.
**** Con el for se le indica a python que colección se quiere
recorrer y que nombre tendrá cada elemento en cada iteración.
"""
)
print("=" * 60)

print("# Bucle FOR\n")

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: 
    print(element)
print("\n" + "-"*50)


my_set = {"geral", "Molopez", 35}

for element in my_set:
    print(element)


print("\n" + "-" * 50)
my_tuple = (35, 1.77, "geral", "lopez", "sanchez")

for element in my_tuple:
    print(element)

print("\n" + "=" * 50)
print("# Los dict solo imprime las claves no los valores\n")

my_dict = {"Nombre": "geral", "Apellido": "lopez", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)

print("\n" + "-" * 80)
print("""
* Para recorrer unicamente los valores de un diccionario se utiliza el método .values()      
** Si se desean recorrer tanto las claves como las valores,se utiliza el metodo .items()
""")

for element in my_dict.values():
    print(element)
else:
    print("el bucle for para diccionario ha finalizado")

print("\n" + "-" * 80)
print(
"""
- Uso de FOR , CONTINUE , Y ELSE con diccionarios: 
* CONTINUE permite saltar la continuación del código y pasar la siguiente iteración del bucle
** El bloque 'else' de FOR se ejecuta cuando el bucle termina de forma natural sin interrupciones
con 'break'.
"""
)
print("\n" + "-" * 80)

for element in my_dict:
    print(element)

    if element == "Edad":
        continue
else:
    print("El bucle for para diccionario ha finalizado")

