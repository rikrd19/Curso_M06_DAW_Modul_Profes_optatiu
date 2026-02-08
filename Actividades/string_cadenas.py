print("----------------------------------------------")
print("String")
print("----------------------------------------------\n")
my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print("----------------------------------------------")
print(len(my_other_string))
print("----------------------------------------------")
print(my_string + my_other_string)
print("----------------------------------------------")
print(my_string + " " + my_other_string) # para agregar un espacio entre string
print("----------------------------------------------")
mi_new_line_string = "Este es un string\ncon salto de linea" 
print(mi_new_line_string)
print("----------------------------------------------")
mi_new_line_string_tabuladorYSalto = "Este es un string\n\tcon salto de linea" # tambien se puede colocar mas de un caracter especialprint(mi_new_line_string)
print(mi_new_line_string_tabuladorYSalto)
print("----------------------------------------------")
my_escape_string =  "Este es un string\\ncon salto de linea"
print(my_escape_string)
print("----------------------------------------------")

name, surname, age = "Ricardo", "Avila", 58
print("Mi nombre es " + name + "  " + surname + " y mi edad es "+ str(age))
print("----------------------------------------------\n")

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

print("\n----------------------------------------------")
print("Formateo con el metodo format")
print("----------------------------------------------")
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))

print("\n----------------------------------------------")
print("Formateo  moderno con el metodo f-string")
print("----------------------------------------------\n")
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

print("\n----------------------------------------------")
print("Desempaquetado de caracteres en python")
print("----------------------------------------------")
languaje = "Python"
a, b, c, d, e, f = languaje
print(a)
print(e)

print("\n----------------------------------------------")
print("Division(slicing) de cadenas")
print("----------------------------------------------")


# Continuacion de Strings

language = "Python"

language_slice = language[1:3]
print(language_slice)  # Output: yt

language_slice = language[1:]
print(language_slice) # Output: ython

language_slice = language[-2]
print(language_slice) # Output: o

print("\n---------------- reverse ------------------------------")
# como invertir una cadena en python
language_reversed = language[::-1]
print(language_reversed)  # Output: nohtyP

print("\n---------------- Funciones ------------------------------")
print(language.capitalize())  # Primera letra en mayuscula
print(language.upper())      # Todo en mayuscula
print(language.isnumeric())   # Verifica si es numerico
print(language[1].isnumeric())   # 
print(language.lower())      # Todo en minuscula
print(language.count("t"))  # Cuenta cuantas veces aparece el caracter
print(language.islower())   # Verifica si todo es minuscula
print(language.isupper())   # Verifica si todo es mayuscula
print(language.startswith("py"))  # Verifica si empieza con el valor
print(language.endswith("on"))    # Verifica si termina con el valor
print(language.replace("thon", "py"))  # Reemplaza una parte de la cadena
print(language.find("t"))    # Busca la posicion del caracter




