print("\n ** Condicionales: estructuras que permiten que un programa tome decisiones.") 

my_condition = True

if my_condition:
    print("Se ejecuta la condicion del if\n")

print ("La ejecucion continua")

print("\n--- indentacion: los bloque de codigo no delimitan con {} \n")

my_condition = 5 * 2 # resultado = 10

if my_condition == 11: #si la condicion es 'false' no se ejecuta
    print("Se ejecuta la condicion del segundo if\n")


my_condition = 5*2 # resultado = 10

if my_condition == 10: # si la condicion es 'true' se ejecuta
    print("Se ejecuta la condicion del segundo if\n")




print("""\n** ¿Qué hace 'else' en un una condición?")
    si la condition del if es verdadera se ejecuta el if
    si la condition del if es falsa   se ejecuta el else
    """)

if my_condition > 10: 
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

print("La ejecucion continua")
        
print("""\n** Más de una condición 'and', 'or' y 'not'
- operadores que permiten combinar varias expresiones y decidir si un
bloque de código debe ejecutarse solo cuando todas las condiciones se
cumplan
""")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa")      

print("\n** ¿Qué es 'elif' en una condicion?")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa")


print("""\n** String vacios en condicionales (if my_string:)")
    - algunas cosas se consideran 'False' de forma automática
    cuando se evalúan en un if
""")
print("--- cadena(string) vacia("")")

my_string = ""

if my_string: 
    print("Mi cadena de texto es vacia")

print("--- Uso de 'not' en condicionales con strings")

my_string = "Mi cadena de texto"

if not my_string:
    print("mi cadena de texto es vacia") 

print(""" -- la cadena NO esta vacia, asi que:
    my_string --> True
    
    not my_string --> False
""")