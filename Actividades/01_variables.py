print(" # Hello World --> esto es un comentario. ")
print("Hello Python")

print("\n----- Tipos de datos en Python -----")

mi_lista = [1, "hola", 3, 5.89, True,[2, "star", False]] 
mi_tupla = (1, "hola", 3, 5.89, True)
mi_conjunto = {11, 2, 3, 3, 4}
print(mi_lista)
print(mi_tupla)
print(mi_conjunto)

print("\n------   Consultar tipo de dato -----")
print(type("hola python"))
print(type(5))
print(type(5.89))
print(type(True))
print(type(3 + 1))

print("\n------   Consultar tipo de dato -----")
my_string_vatriable = "Hola Python"
print(my_string_vatriable)

MyVariable = "My String Variable"
print(MyVariable)

mi_int_variable = 5
print(mi_int_variable)

my_bool_variable = False
print(my_bool_variable)

print (my_string_vatriable, MyVariable, mi_int_variable, my_bool_variable)

my_string_vatriable = 5
print (my_string_vatriable)

my_int_to_str_variable = str(mi_int_variable)
print(type(my_int_to_str_variable))

print("\n------ Conversiones de tipos de datos -----")
mi_int = 5
print(type(mi_int))

mi_float = float(mi_int)
print(type(mi_float))

mi_bool = bool(mi_int)
print(type(mi_bool))

print(len(MyVariable))

print("\n------  Uso de variables en print() -----\n")

name,surname,alias,city = "Ricardo","Avila","Richilin","Tarragona"
print("me llamo", name, "mi apellido", surname, "mis amigos me llaman", alias, "y vivo en", city)

print("\n------  Uso de input() -----\n")
first_name = input("Cual es tu nombre?: ")
print("Hola", first_name)

city = input("Cual es tu ciudad?: ")

print("Hola " + first_name + " de " + city)

print("\n")
name = "Ricardo"
age = 58
print("Hola %s, tienes %d, años" % (name, age))


print("\n-------  forzar el tipo de dato  -------\n")
address = str("Mi direccion es calle Falsa 123")
print(type(address))
address = 32
print(type(address))
address = True
print(type(address))    
address = 5.89
print(type(address))