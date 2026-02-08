print("-------  Comparacion de cadenas  -------\n")
print("\n ------ 1. ¿Qué resultado obtuviste en cada comparación?:\n- Se están comparando dos cadenas de usando comparadores relacionales -------\n")
print("Hola" > "Python") # False
print("Hola" < "Python") # True
print("Hola" >= "Python") # False
print("Hola" <= "Python") # True
print("Hola" == "Python") # False
print("Hola" != "Python") # True

print("\n ------ 2. ¿Por qué “Hola” < “Python” devuelve True y “Hola” > “Python” devuelve False? -------\n")
print("- La comparación de cadenas en Python es lexicográfica, basada en el orden de los\n caracteres Unicode (o ASCII).")
print("Hola" < "Python") # True
print("H ('72') < P ('80')") # True

print("Python" > "Hola")    # False
print("P ('80') > H ('72')") # False

# "Hola" -> 'H' (72), 'o' (111), 'l' (108), 'a' (97) 
# "Python" -> 'P' (80), 'y' (121), 't' (116), 'h' (104), 'o' (111), 'n' (110)


print("\n.----- 3. ¿Qué sucede si cambias “Hola” por el string “hola” (con minúscula)?\n")
print("- En ASCII y Unicode, las letras mayúsculas tienen valores numéricos más bajos\n que las letras minúsculas. Por lo tanto, cualquier cadena que comience con una letra\n minúscula será considerada mayor que una cadena que comience con una letra mayúscula.\n")
print("hola" > "Python") # —------> True
print("hola" < "Python") # —------> False
print("hola" >= "Python") # —------> True
print("hola" <= "Python") # —------> False
print("hola" == "Python") # —------> False
print("Hola" != "Python") # —------> True

print("\n------   4. ¿Por qué “Hola” == “ hola” da False aunque parecen iguales?\n")
print("- El resultado es False.")
print("- Nuevamente la comparación de cadenas en Python es lexicográfica, basada en el")
print("orden de los caracteres Unicode (o ASCII).")
print("- Donde se compara carácter a carácter el valor unicode de cada uno:")
print("- h (minúscula) = 104 y H (mayúscula) = 72, donde siempre ‘h’ minúscula va a ser")
print("mayor que ‘H’ mayúscula.")

print("\n------  5. ¿Qué crees que hace Python internamente para comparar dos textos?\n")
print("- Internamente Python compara caracter a caracter;")
print("- 'H' = 72 'P' = 80")
print("- 'h' = 104 'o' = 111")
print("- 'l' = 108 'y' = 121")
print("- 'a' = 97 't' = 116")

print("- \"Hola\" vs \"Python\" → Se detiene en 'H' vs 'P'")
print("- No evalúa 'o' vs 'y', 'l' vs 't', etc.")
print("- \"Python\" vs \"Py\" resultado \"Python\" > \"Py\" el primer string")
print("es más largo después del prefijo común, con lo cual al sumar")
print("\nsus valores de cada caracter es mayor.")
print("\n- Optimizaciones internas: \n")
print("- Short-circuit evaluation: Se detiene en la primera diferencia")
print("- Hash caching: Python puede cachear hashes para comparaciones frecuentes")
print("- Interning: Para strings pequeños, Python usa \"interning\" para comparaciones más")
print("rápidas por identidad")


print("\n--------- 6. 7. 8. Escribe en el intérprete lo siguiente y anota el resultado:")
print("Al ejecutar: print(ord(\"H\")) –—--------> 72")
print("print(ord(\"P\")) —----------> 80")
print("● ord(): Convierte carácter → número Unicode")
print("Los números que devuelve ord() representan los puntos de código Unicode (equivalente a")
print("ASCII para caracteres básicos), qué significan:")
print(ord("H")) # 72 → Punto de código Unicode para 'H'
print(ord("P")) # 80 → Punto de código Unicode para 'P'


print("\n------- 9. Cambia las palabras y prueba con ejemplos como:")
print("print(\"a\" < \"b\") —-------------> True")
print("- 'a' tiene un valor Unicode de 97 y 'b' tiene 98. Cómo 97 < 98, entonces \"a\" es menor\n")

print("que \"b\", por lo tanto True.")
print("print(\"Z\" < \"a\") —-------------> True")
print("- 'Z' es mayúscula y tiene un valor de 90, mientras que 'a' minúscula tiene 97. Como")
print("90 < 97, entonces True.\n")

print("Casa" > "casa") #—------> False
print("- Se compara el primer carácter: 'C' (mayúscula) valor 67 vs 'c' (minúscula) valor 99.")
print("Cómo 67 < 99, entonces \"Casa\" es menor que \"casa\", por lo tanto la comparación da")
print("False.\n")

print("Python" > "Py") #-----------> True
print("Primero se comparan los primeros dos caracteres: 'P' con 'P' (iguales), luego 'y' con 'y' (iguales).")
print("# Pero como el string \"Python\" tiene más caracteres: el tercer carácter de \"Python\" es")
print("# 't' y \"Py\" no tiene tercer carácter.")
print("Se asume que “Py”, puede ser un prefijo de “Python”, por lo tanto la cadena que es")
print("más corta que la otra , la cadena más larga es mayor.")
print("Por lo tanto:")

print("Python > Py es True.")