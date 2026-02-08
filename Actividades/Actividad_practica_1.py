## Prácticas Ejercicios ##
print("\n===== Parte 1 =====\n")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa un tu edad: "))
number_float = float(input("Ingresa un tu peso: "))
es_estudiante = input("Eres estudiante (si/no): ")
print("Hola mi nombre es: ", nombre)
print("Mi edad es :", edad)
print("Mi peso es :", number_float)
print("Soy estudiante de Ilerna:", es_estudiante)

print("\n=====Tipos de datos =====\n")
print(type(nombre))
print(type(edad))
print(type(number_float))
print(type(es_estudiante))


print("===== Parte 2 =====")
gustos= input("Ingresa tu fruta favorita,tu música, el signo zodiacal, un número (separadas por comas):):")
lista_frutas = gustos.split(",")
print("Tu fruta favorita es:", lista_frutas)


print("\n===== Parte 3 =====\n")
comidas_favoritas = ("Pizza", "Pasta", "Sushi", "Helado", "Tacos")
print("Comidas favoritas:", comidas_favoritas)
print("Las comidas favoritas son:",len(comidas_favoritas))
print("Al querer cambiar una posición de la tupla da error porque las tuplas son inmutables")

print("\n")
# comidas_favoritas[0] = "Hamburguesa"
# print("Comidas favoritas:",comidas_favoritas)
# print(len(comidas_favoritas)) # TypeError: 'tuple' object does not support item assignment


print ("\n===== Parte 4 =====\n")

numeros = {1, 2, 2, 3, 4, 4, 5}
print("Conjunto de numeros:", numeros)
print("""
** Los conjuntos (set) no permiten elementos duplicados - Cada elemento es único
** No mantienen un orden específico - Los elementos pueden aparecer en cualquier orden
""")
numeros = numeros | {6}


print("Conjunto de numeros:", numeros)

print ("\n===== Parte 5 =====\n")

print(type(nombre))
print(type(gustos))
print(type(comidas_favoritas))
print(type(numeros))
resumen = [gustos, comidas_favoritas, numeros]
print(resumen)


print("\n======Parte 6 – Reto de lógica ======\n")
# 1. Usa la edad que guardaste en la parte 1.
# 2. Escribe un bloque de código que imprima un mensaje diferente según la
# edad:

# o Si la edad es menor de 18: muestra “Eres menor de edad”.
# o Si la edad es entre 18 y 30: muestra “Eres joven”.
# o Si es mayor de 30: muestra “Eres adulto”.
# 3. Usa operadores lógicos (and, or) para combinar condiciones.
# 4. Explica en un comentario qué hace tu código y por qué.
# Pista: Recuerda que puedes usar la estructura if, elif y else.

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad <= 30:
    print("Eres joven.")
elif edad > 30:
    print("Eres adulto.")

print("** Mediante un condicional if, elif podemos clasificar a las personas segun su rango de edad")

