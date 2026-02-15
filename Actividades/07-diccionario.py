
print(""" --- Dicts (Diccionarios) ---
- estructura de datos que almacena información mediante
    pares clave-valor
- donde cada clave sirve para acceder a su valor
    """)  

print("\n --- uso del constructor dict() ---")
my_dict = dict()
print(type(my_dict))

print("\n --- uso de llaves {} para crear un diccionario ---")
my_other_dict = {}
print(type(my_other_dict))


print("\n --- Diferencia diccionario: de distintos tipos ---")

my_other_dict = {
    "Nombre": "Geral",
    "Apellido": "Lopez",
    "edad": 35, 
    1: "Python"} #clave  nombre - el valor informacion Geral

print("\n --- Permite guardar colecciones de elementos en una sola clave")

my_dict = {
    "Nombre": "Geral",
    "Apellido": "Lopez",
    "edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"}
}

print("\n --- funcion len(): cuenta los elementos reales del contenedor ---")
print(len(my_other_dict))
print(my_dict)

print("\n --- Ventajas de los diccionarios permiten acceder directamente ---")
print(my_dict["Nombre"])

print("\n --- modificar un valor en un diccionario ---")
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print("\n --- agregar una nueva clave con su valor a un diccionario ---")
my_dict["Calle"]="Calle nou"
print(my_dict)

print("\n --- eliminar un elemento concreto de un diccionario ---")
print(my_dict)
del my_dict["Calle"] # si se quiere borrar una sola clave con su valor
print(my_dict)

print("\n --- elimina el diccionario completo no un elemento ---")
# del my_dict

print("\n --- que pasa si se usa 'in' ---")
print("\ngeral" in my_dict) # "Geral" no es una clave , es un valor falso
print("Nombre" in my_dict)

print("\n --- mas métodos de los diccionario ---")
print(my_dict.items()) # devuelve pares clave- valor
print(my_dict.keys()) #devuelve solo las claves del diccionario
print(my_dict.values()) # devuelve solo los valores del diccionario


print("\n --- metodo fomkeys() en diccionarios ---")
print("(en la práctica no resulta muy útil porque no conserva los datos del diccionario original.)")
my_new_dict = my_other_dict.fromkeys(("Nombre", 1)) # crea un nuevo dicionario con esas claves y valor None
print(my_new_dict)

print("\n--- puede generar todas las claves en una sola linea de codigo"
" sin tener que escribirla una por una ---")
my_new_dic = dict.fromkeys(my_dict)
print(my_new_dict)
