print("\n ***** Tuplas *****")

print("\n---------------- constructor tuple() -----------------")
my_tuple = tuple((35, 1.72, "Ricardo", "Lopez"))

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

my_tuple = []

print("\n-------------- metodo .count() ----------------")
my_tuple = (34, 3, 1, "avila", 3, "ricardo", 3)
print(my_tuple.count("avila"))
print(my_tuple.count("ricardo"))
print(my_tuple.count(3))

print("\n------------ metodo .index() ---------------")
print(my_tuple.index("avila"))
print(my_tuple.index("ricardo"))

print("\n------------ metodo .count() e index() funcionan igual en tuplas y listas ---------------")
print("my_tuple[1] = 1.72")
print("print(my_tuple) #*** no se puede cambiar el elemento ya que las tuplas son inmutables")

print("\n------------- concatenacion de tuplas -------------") 
my_tuple = (3, 6, "casa", 45, "hotel", 100)
my_other_tuple = ("ricardo", 4, 6, "hotel")

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print("\n------------ convertir una tupla en lista ------------") 
my_tuples = list(my_tuples)
print(type(my_tuples))

my_tuple2[2] = "Ilerna"

my_tuples.insert(1, "Azul")

print(my_tuples)


print("""\n---  operador 'del' sirve para eliminar elementos o variables
---  pero en tuplas se borran todos los elementos -------\n""")

my_tuple = ("a", "b", "c", 3, 6, 8, 9, "home")
print("""del my_tuple[2] *** No permite eliminar el elemento
las tuplas no se modifican o permite agregar elementos\n""")
del  my_tuple
print ("""print(my_tuple) ** NameError: name 'my_tuple' is not defined
porque la toda la variable fue eliminada \n""")


