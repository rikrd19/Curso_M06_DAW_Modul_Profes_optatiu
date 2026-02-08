print("\n****  Listas ****")
# Una lista en Python estructura de datos que permite almacenar
# varios elementos dentro de una sola variable.
# una lista no
# es un tipo simple, sino un contenedor que puede guardar muchos valores.

my_list = list()
my_other_list = []

print("\n------  Cuántos elementos hay en cada lista ------------\n")
print(len(my_list))
print(len(my_other_list))

print("\n------  Elementos de la lista ------------\n")
my_list = (35, 24, 62, 52, 30, 30,17)
print("Los elementos de la lista son:", my_list)
print(len(my_list))

print("\n------  funcion type ------------\n")
my_other_list = [35, 160, 160,"Ricardo", "Avila"]
print (type(my_other_list))


print("\n------  Accceder a los elementos de la lista ------------\n")
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[3])

print("\n------  Accceder a los elementos de la lista por indices negativos------------\n")
print(my_other_list[-1]) # muestra el ultimo elemento 
print(my_other_list[-2]) # muestra el penultimo elemento

print("\n------ Al acceder a los elementos de la lista, si no existen: error ------------\n")
print("my_other_list[4])  # IndexError: list index out of range ")

print("\n------ metodo .count() ------------\n")

print(my_other_list.count("Ricardo")) # resultado 1
print(my_other_list.count(160)) # resultado 2


print("\n------ desempaquetado de listas ------------")
age, heigth, name, surname = my_other_list[0], my_other_list[1], my_other_list[3], my_other_list[4]
print(age)
print(name)

print("\n------ concatenacion de listas ------------\n")
my_list = (35, 24, 62, 52, 30, 30,17)
my_other_list = (35, 160, 160,"Ricardo", "Avila")
print(my_list + my_other_list)

print("\n------ No se necesita indicar el tipo de la lista ------------\n")

my_list = "Hola Python"
print(my_list)
print(type(my_list))

my_list = (35, 24, 62,52, 30,30,17)
print(type[my_list])


print("\n------ Agregar elementos a la lista con .append() ------------\n")
#es un método propio de las listas en Python que
#se utiliza para agregar un elemento al final de una lista existente.
my_other_list = []
my_other_list.append("Ilerna")
print(my_other_list)

my_other_list = [1,2,"Home", 150]
my_other_list.append("Ilerna")
print(my_other_list)

print("\n------ Agregar elementos a la lista con .insert() ------------\n")
# se utiliza para insertar un nuevo elemento en una
# posición específica dentro de una lista.
# A diferencia de .append(), que siempre agrega al final, .insert() nos
# permite elegir el lugar exacto donde queremos colocar el nuevo valor.
my_other_list.insert(1, "Azul")
my_other_list.insert(2, "Azul")
my_other_list.insert(5, "Azul")
print(my_other_list)

print("\n------ Estructuras mutables en listas ------------\n")
# significa que podemos cambiar sus elementos después de crearlas.
# Esto se puede hacer accediendo directamente a una posición
# (índice) y asignándole un nuevo valor.
my_other_list[1] = "Rojo"
print(my_other_list)

print("\n------ Operador .remove() ------------\n")
# se puede utilizar en listas de números.Este método elimina el primer 
# elemento que coincida con el valor indicado dentro de la lista.
my_list = [10, 20, 30, 40, 50]  
print("Mi lista: ",my_list)
my_list.remove(30)
print("Mi nueva lista: ",my_list)

print("\n------ Operador .pop() ------------\n")
# se utiliza para eliminar elementos de una lista, pero a
# diferencia de .remove(), trabaja con el índice (posición) del elemento y
# devuelve el valor eliminado.
print(my_list.pop()) # elimina el ultimo elemento
print(my_list)      
print(my_list.pop(2)) # elimina el elemento en la posicion 2
print(my_list)

print("\n------ Operador del ------------\n")
# para eliminar elementos de una lista indicando su posición (índice).
# A diferencia de .remove() o .pop(), del no devuelve el valor eliminado,
# simplemente lo borra.
my_list = [10, 20, 30, 40, 50]  
del my_list[2]
print(my_list)  

print("\n------ Limpiar la lista con .clear() ------------\n")
# se utiliza para vaciar completamente una lista, es
# decir, eliminar todos sus elementos, pero manteniendo la lista
# creada (no la borra del todo).
my_list.clear()
print(my_list)

print("\n------ el metodo .copy() ------------\n")
# El método .copy() permite crear una copia independiente de una lista,
# mientras que .clear() vacía completamente una lista existente sin eliminarla.
# Este ejemplo muestra cómo ambos pueden usarse juntos sin afectar la copia.

# *** Cuando usamos .copy(), creamos una lista nueva e independiente.
# Si luego vaciamos la original con .clear(), la copia mantiene sus datos
# intactos.
# Este comportamiento es muy útil cuando queremos preservar información
# original antes de modificar o reiniciar una lista.
my_new_list = [10, 20, 30, 40, 50]  
print(my_new_list)

my_list = my_new_list.copy()
print(my_list)

print("\n------ Limpiar la lista con .clear() ------------\n")
my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

print("""\n------ metodo reverse ------------\n")
# se utiliza para invertir el orden de los elementos de
# una lista existente. A diferencia de otros métodos, 
# no crea una nueva lista, sino que modifica directamente la original.
my_new_list.reverse()
print(my_new_list """)

print("\n------ metodo .sort() ------------\n")
# se utiliza para ordenar los elementos de una lista, ya sea
# de números o de cadenas de texto. Por defecto, ordena de menor 
# a mayor (o alfabéticamente si son textos).
my_new_list = [10, 80, 60, 20, 30, 79, 40, 50] 
my_new_list.sort()
print(my_new_list)  
    
my_new_string = ["Casa","Bueno", "Tarde", "Python", "Sorteo", "Laptop"] 
my_new_string.sort()
print(my_new_string)