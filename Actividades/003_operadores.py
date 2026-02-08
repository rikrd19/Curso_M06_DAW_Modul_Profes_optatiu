
print("------- Podemos definir una variable tipo string usando comillas simples-------\n")

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + my_other_string)


print("\n-------  podemos agregar un espacio entre las cadenas al concatenarlas. -------\n")
print(my_string + " " + my_other_string)

print("\n-------  existen caracteres especiales que podemos usar dentro de los strings.-------\n")
my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

print("\n------- el carácter especial \\t\\ para agregar una tabulación  -------\n")
my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)


print("\n-------  podemos usar más de un carácter especial en la misma cadena.  -------\n")
my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)


print("\n-------  mostrar una barra invertida (\) dentro de un string, debemos escribir dos barras invertidas (\\\\).-------\n")
my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)


print("\n-------  Formateo con el método .format() -------\n")
name, surname, age = "Geraldin", "Lopez", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))


print("\n------- formateo de cadenas al estilo C, porque viene del lenguaje C.")
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

print("name, surname, age = \"Geraldin\", \"Lopez\", 35")
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

print("\n-------  Formateo con f-strings (cadenas literales formateadas) -------\n")
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


print("\n# Continuacion de Strings")

language = "Python"

language_slice = language[1:3]
print(language_slice)  # Output: yt

language_slice = language[1:]
print(language_slice) # Output: ython

language_slice = language[-2]
print(language_slice) # Output: o

print("\n---------------- reverse: como invertir una cadena en python ------------------------------")

language_reversed = language[::-1]
print(language_reversed)  # Output: nohtyP

print("\n---------------- Funciones ------------------------------")
print(language.capitalize(),  "# Primera letra en mayuscula")
print(language.upper(), "# Todo en mayuscula")
print(language.isnumeric(), " # Verifica si es numerico") 
print(language[1].isnumeric())  
print(language.lower(),      "# Todo en minuscula")
print(language.count("t"),  "     # Cuenta cuantas veces aparece el caracter")
print(language.islower(), " # Verifica si todo es minuscula")
print(language.isupper(),   " # Verifica si todo es mayuscula")
print(language.startswith("py"),  " # Verifica si empieza con el valor")
print(language.endswith("on"),    "  # Verifica si termina con el valor")
print(language.replace("thon", "py"),  "  # Reemplaza una parte de la cadena")
print(language.find("t"),  "     # Busca la posicion del caracter\n")

