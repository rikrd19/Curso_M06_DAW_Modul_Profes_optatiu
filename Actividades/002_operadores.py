print("\n# Operadores #")

print(3 + 4)  # Suma
print(3 - 4)  # Resta  
print(3 * 4)  # Multiplicacion
print(3 / 4)  # Division

print(3 % 4)    # Modulo
print(10 % 3)   # Modulo

print("\n# llamada floor division #")
print(10 // 3)  # Division entera
print(10 // 4)  # Division entera

print("\n# Operador de potencia #")
print(2 ** 3)   # 2^3 = 2*2*2 = 8
print(3 ** 4)   # 3^4 = 3*3*3*3 = 81

print("\n# Operadores de concatenacion #")
print("Hola "  "Python")
print("Hola" , "Python")
print("Hola " + "Python")
print("""# print("Hola" - "Python") #solo funciona con numeros:TypeError: unsupported operand type(s)
# print("Hola" * "Python") #solo funciona con numeros:TypeError: unsupported operand type(s)
# print("Hola " + "Python" +"?Que tal?")
    """)


print("print(\"Hola\" + 5) #TypeError: can only concatenate str (not \"int\") to str)")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * int(2.5))  # convierte el float a int y lo multiplica