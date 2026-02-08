# Escribe un programa en Python que almacene una palabra en
#  la variable language y muestre por pantalla la siguiente
# información utilizando métodos de cadenas:

# Nota: Todos
# los resultados deben mostrarse con print().

language = "Meteorologia"


print("\n--------  1. La palabra con la primera letra en mayúscula.")
print(language.capitalize())


print("\n--------  2. La palabra completamente en mayúsculas.")
print(language.upper())

print("\n--------  3. Cuántas veces aparece la letra 'o' en la palabra.")
print(language.count("o"))


print("--------  4. Si la palabra está formada únicamente por números.")
print(language.isnumeric())

print("\n--------  5. Una comprobación numérica usando el texto '1'.")
print(language[1].isnumeric())

print("\n--------  6. La palabra en minúsculas.")
print(language.lower())


print("\n--------  7. Si la palabra está completamente en mayúsculas.")
print(language.isupper())

print("\n--------  8. Si la palabra comienza con 'Mete'.")
print(language.startswith("Mete"))                            

print("\n--------  9. Si la palabra termina con 'ia'.")
print(language.endswith("ia"))   

print("\n--------  10. Si la palabra se reemplaza con una parte de la cadena")
print(language.replace("gia", "py"))  

print(language.find("t"))    # Busca la posicion del caracter
