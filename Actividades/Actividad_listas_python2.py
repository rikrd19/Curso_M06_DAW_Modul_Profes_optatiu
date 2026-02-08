# Actividad: Gestionamos información con Listas en Python
# Objetivo:
# Practicar la creación y manipulación de listas en Python 
# aplicando operaciones
# básicas, métodos integrados y acceso mediante índices.
# Instrucciones:

# 1. Crea un nuevo archivo en tu entorno de trabajo llamado
# actividad_listas2.py.



# 2. Declara una lista llamada precios que contenga al menos seis valores
# numéricos (pueden representar precios de productos o servicios).
# o Asegúrate de incluir al menos un valor repetido.
print("\n------ Lista de precios ------------\n")
lista_precios = [100.00, 30.00, 200.00, 150, 200.00, 400.00, 50]
print(lista_precios)

# 3. Crea otra lista llamada empleado con cuatro datos distintos:
# - nombre, edad, puesto de trabajo y ciudad.
# (Ejemplo: ["Lucía", 29, "Diseñadora", "Barcelona"])
print("\n------ Lista de empleado ------------\n")
lista_empleado = ["Carlos", 35, "Desarrollador", "Madrid"]
print(lista_empleado)

# 4. Analiza las listas:
# - Muestra ambas listas con print().
print("\n------ Mostrando Ambas listas ------------\n")
print("Lista de precios:", lista_precios)
print("Lista de empleado:", lista_empleado)

# - Usa len() para mostrar cuántos elementos tiene cada lista.
print("\n------ Uso de len() ------------\n")
print("Numeros de lementos lista Precios: ", len(lista_precios))
print("Numeros de elementos lista Empleado: ", len(lista_empleado))

# - Usa type() para verificar el tipo de dato.
# 5. Accede a elementos específicos:
print("\n------ Uso de type() ------------\n")
print(type(lista_precios))
print(type(lista_empleado))


# - Muestra el primer, tercer y último elemento de la lista empleado.
print("\n------ Accediendo a elementos específicos de la lista Empleado ------------\n")
print("Primer elemento lista Empleado:", lista_empleado[0])
print("Tercer elemento lista Empleado:", lista_empleado[2])
print("Último elemento lista Empleado:", lista_empleado[-1])


# - Usa índices negativos para acceder al penúltimo elemento.
print("\n------ Accediendo a elementos específicos de la lista Empleado ----------\n")
print("Penúltimo elemento lista Empleado:", lista_precios[-2])
print("Penúltimo elemento lista Empleado:", lista_empleado[-2])


# 6. Actualiza información:
# - Cambia la ciudad o el puesto de trabajo del empleado.
lista_empleado = ["Carlos", 35, "Desarrollador", "Madrid"]
print("\n------ Cambiando el puesto de trabajo y la ciudad ----------\n")
lista_empleado[2] = "Arquitecto"
print(lista_empleado)

lista_empleado[3] = "Valladolid"
print(lista_empleado)


# - Agrega un nuevo elemento con .append() (por ejemplo, un departamento o área).
print("\n------ Agregando a la lista un nuevo elemento ----------\n")
lista_empleado.append("Tarragona")
print(lista_empleado)

lista_empleado.append("2550 mts2")
print(lista_empleado)


# - Inserta un nuevo dato en la segunda posición con .insert() (porejemplo, un número de empleado).
print("\n------ Agregando elemento con insert ----------\n")
lista_empleado.insert(1, "email")
print(lista_empleado)


# 7. Elimina información:
# - Usa .remove() para quitar un precio específico de la lista precios.
print("\n------ Eliminando información específica ----------\n")
lista_precios = [100, 30.00, 200.00, 150, 400, 50]
lista_precios.remove(200.00)
print(lista_precios)


# - Usa .pop() para eliminar el último precio e imprimir el valor eliminado.
print("\n------ Eliminando información específica con .pop() ----------\n")
print(lista_precios.pop())
print("Lista actual: ", lista_precios)


# - Usa del para eliminar el segundo elemento de la lista empleado.
print("\n------ Eliminando el segundo elemento de la lista empleado ----------\n")
lista_empleado = ["Carlos", 35, "Desarrollador", "Madrid"]
del lista_empleado[1]
print("Lista actual de empleado: ", lista_empleado)


# 8. Combina listas:
# - Crea una nueva lista llamada datos_empresa que combine empleado y precios usando el operador +.
print("\n------ Combinando listas ------------\n")
datos_empresa = lista_empleado + lista_precios
# - Muestra el resultado.
print("Lista combinada datos_empresa: ", datos_empresa)


# 9. Aplica métodos de listas:
# - Usa .count() para contar cuántas veces se repite un mismo precio.
print("\n------ Contando elementos en la lista de precios ------------\n")
lista_precios = [200.00, 100, 30.00, 200.00, 150, 400, 50, 200.00]
print("El precio 200.00 se repite: ", lista_precios.count(200.00), " veces")


# - Usa .copy() para duplicar la lista precios antes de vaciarla con .clear().
print("\n------ Copiando y limpiando la lista de precios ------------\n")
lista_precios_copiada = lista_precios.copy()
lista_precios.clear()
# - Imprime ambas listas para comparar.
print("Lista de precios copiada: ", lista_precios_copiada)
print("Lista de precios original después de clear(): ", lista_precios)


# 10. Ordena y reorganiza:
# - Crea una lista llamada ventas con números enteros y ordénala de menor a mayor con .sort().
print("\n------ Ordenando la lista de ventas ------------\n")
ventas = [500, 150, 300, 450, 200, 100]
ventas.sort()
print("Lista de ventas ordenada: ", ventas)


# - Luego invierte el orden con .reverse() y muestra el resultado final.
print("\n------ Invirtiendo la lista de ventas ------------\n")
ventas.reverse()
print("Lista de ventas invertida: ", ventas)


# Crea una lista llamada lenguajes con los lenguajes de programación que te gustaría aprender.
print("\n------ Lista de lenguajes de programación ------------\n")
lenguajes_programacion = ["Python", "JavaScript", "Go", "Rust", "Kotlin"]
print("Lista de lenguajes a aprender: ", lenguajes_programacion)


# - Muestra solo los dos primeros usando slicing ([:2]).
print("\n------ Mostrando los dos primeros lenguajes ------------\n")
print("Dos primeros lenguajes: ", lenguajes_programacion[:2])


# - Cambia uno por otro que ya conozcas.
print("\n------ Cambiando un lenguaje por otro ------------\n")
lenguajes_programacion[2] = "Java"
print("Lista actualizada de lenguajes: ", lenguajes_programacion)

# - Agrega un nuevo lenguaje al final y elimina el primero.
print("\n------ Agregando y eliminando lenguajes ------------\n")
lenguajes_programacion.append("C#")
print("Después de agregar un nuevo lenguaje: ", lenguajes_programacion)
del lenguajes_programacion[0]
print("Después de eliminar el primer lenguaje: ", lenguajes_programacion)

    
# Resultado esperado:

# El programa debe:
# -  Mostrar el contenido y tipo de las listas correctamente.
# -  Modificar, eliminar y agregar elementos sin errores.
# - Combinar listas y aplicar correctamente métodos como .append(), .insert(),
# .remove(), .pop(), .count(), .copy(), .clear(), .sort() y .reverse().
# - Demostrar comprensión del acceso mediante índices positivos y negativos.