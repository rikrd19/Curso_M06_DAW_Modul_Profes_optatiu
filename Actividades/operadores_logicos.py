
print("----------------------------------------------")
print("Ejercicios Operadores Logico")
print("----------------------------------------------")
print("----------------------------------------------")
print("Ejercicio 1")
print("----------------------------------------------")


print("Home" > "Casa")
print("Home" < "Casa")
print("Home" >= "Casa")
print(len("a123") >= len("a1234"))
print("Home" <= "Casa")
print("Home" == "Casa")
print("\n----------------------------------------------")
print(5 >  6 and  "Home" > "Casa") 
print(5 >  6 or  "Home" > "Casa") 
print(5 <  6 and  "Home" > "Casa") 
print(5 <  6 or  "Home" > "Casa") 


print("----------------------------------------------")
print("precedencia")
print("----------------------------------------------\n")
print (1 < 2 or ("Hola" > "Python" and 4 == 4)) #true 
print (1 < 2 or ("Hola" < "Python" or 4 == 4)) #true
print (1 > 2 and ("Hola" < "Python" and 4 == 4)) #false
print ((1 < 2 or "Hola" > "Python") and 4 == 4) # true
print (1 < 2 or ("Hola" > "Python") and 4 != 4) # true
print("----------------------------------------------\n")

print("----------------------------------------------")
print("Operador not")
print("----------------------------------------------\n")
print(not("Hola" > "Gato")) # resultado false ---> "H" no es mayor que "G"
print(not("Hola" < "Gato")) # Resultado true ----> "H" es menor que "G"
print(not("Hola" < "Gato") or 3 > 4) # Resultado true 
print(("Hola" < "Gato") and ("Gato" and "Hola") or (not(3 > 4))) # Resultado false ---->  
print("Hola" < "Gato" and (not(3 > 4))) # False
print("Hola" > "Gato" and (not(3 > 4))) # False