print("\n***** Sets *****\n")
print("\n-- SI SE USA LLAVE VACIA {} PYTHON LA INTERPRETA COMO DICCIONARIO ---")

print("""\n----- Conjunto 'set' es una colección de elementos -----
    - No tiene orden específico 
    - No permmite duplicados: almacena valores únicos, se define con llaves '{}'
    - Si la llave se usa vacia '{}' se interpretara como diccionario
""")

my_set = set()
my_other_set = {} # si se usa llave vacia python la interpreta como diccionario

print(type(my_set))
print(type(my_other_set))


print("\n ---- Método  'len()' para ver cuantos elementos tenemos dentro del sets -----")
my_other_set = {"Lima", "Avila"," Bogotá", "Madrid", 100, 200, 300}
print(len(my_other_set))


print("\n***** Diferencias entre sets, lista y tuplas *****\n")

print("------ Método 'add()' -------")
my_other_set.add("Ricardo")
print(my_other_set)


print("\n----- El conjunto 'set'  NO reconoce elementos repetidos  ------")

my_other_set = {"Avila", "Luis", "Ricardo", 50, "Luis"}
print(type(my_other_set))

my_other_set.add("Avila")
print(my_other_set)

print("\n--- Podemos mirar si tenemos un elemento dentro del conj. set y me arroja false o true -----")
print("Ricardo" in my_other_set) # esto imprimira True
print("Perez" in my_other_set) # esto imprimira False

print("\n----- Eliminar elementos de un set con .remove() -----")
my_other_set = {"Python", "Avila", "Developer"}
my_other_set.remove("Avila")
print(my_other_set)

print("\n-----  vaciar un set completo  .clear() ----")
my_other_set.clear()
print(my_other_set) # imprimira un set vacio 'set()' manteniedo la variable

print("\n------  Eliminar por completo la variable de un set con 'del'  -------")
my_other_set = {"red", "blue", "green"}
print(f"El set antes de ser eliminado: {my_other_set}")

del my_other_set

print("si se intenta imprimir la variable, dara 'NameError' porque ya no existe.")

print("\n-------  convertir un set en list -------")
my_set = {"Avila", "Ricardo", 35}
my_list = list(my_set)
print(my_list)

print("\n-------  unir conjuntos con .union() --------")
my_other_set = {"java", "php", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

