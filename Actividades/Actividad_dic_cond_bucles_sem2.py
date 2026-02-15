# Desarrollar un programa que gestione alumnos utilizando diccionarios, condicionales
# y bucles, simulando un pequeño sistema académico.


print(" ******** Parte 1 ********\n")

print("------ Estructura inicial de datos ------")

alumnos = {}

alumnos["ana"] = {
    "edad": 19,
    "curso": "DAW",
    "lenguajes": {"Python", "Java"},
    "nota": 7.5,
}

alumnos["jose"] = {
    "edad": 20,
    "curso": "DAM2",
    "lenguajes": {"PHP", "React"},
    "nota": 5.0,
}

alumnos["alberto"] = {
    "edad": 18,
    "curso": "DAM2",
    "lenguajes": {"HTML", "GitHub"},
    "nota": 6.5,
}

alumnos["carlos"] = {
    "edad": 17,
    "curso": "DAM2",
    "lenguajes": {"JavaScript", "Python"},
    "nota": 6.5,
}

alumnos["alicia"] = {
    "edad": 18,
    "curso": "DAM2",
    "lenguajes": {"Java", "PHP"},
    "nota": 9.0,
}


print("\n******** Parte 2 - Mostrar Alumnos ********\n")

for nombre, datos in alumnos.items():
    print(f"Alumno: {nombre.capitalize()}")
    print(f"Edad: {datos['edad']}")
    print(f"Curso: {datos['curso']}")
    print(f"Lenguajes: {', '.join(datos['lenguajes'])}")
    print(f"Nota media: {datos['nota']}")
    print()


print("\n******** Parte 3 - Condicionales sobre notas ********\n")

for nombre, datos in alumnos.items():
    nota = datos["nota"]
    estado_nota = ""
    if nota < 5:
        estado_nota = "Suspenso"
    elif 5 <= nota < 7:
        estado_nota = "Aprobado"
    elif 7 <= nota < 9:
        estado_nota = "Notable"
    else:  # nota >= 9
        estado_nota = "Sobresaliente"

    print(f"Alumno: {nombre.capitalize()} - Nota: {nota} ({estado_nota})")
print()


print("\n******** Parte 4 - Filtrar por Alumnos ********\n")

for nombre, datos in alumnos.items():
    if datos["edad"] >= 18 and datos["nota"] >= 7:
        print(
            f"Alumno mayor de 18 y con nota mayor o igual a 7: {nombre.capitalize()}\n"
        )


print("\n******** Parte 5 - While con Menú ********\n")

while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar alumnos")
    print("2. Buscar alumno")
    print("3. Añadir alumno")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- Lista de Alumnos ---")
        if not alumnos:
            print("No hay alumnos registrados.")
        for nombre, datos in alumnos.items():
            print(
                f"- {nombre.capitalize()} (Curso: {datos['curso']}, Nota: {datos['nota']})"
            )

    elif opcion == "2":
        nombre_buscar = input("Nombre del alumno a buscar: ").lower()
        if nombre_buscar in alumnos:
            datos = alumnos[nombre_buscar]
            print(f"\nDatos de {nombre_buscar.capitalize()}:")
            print(f"Edad: {datos['edad']}")
            print(f"Curso: {datos['curso']}")
            print(f"Lenguajes: {', '.join(datos['lenguajes'])}")
            print(f"Nota: {datos['nota']}")
        else:
            print(f"El alumno '{nombre_buscar}' no existe.")

    elif opcion == "3":
        nombre_nuevo = input("Nombre del nuevo alumno: ").lower()
        if nombre_nuevo in alumnos:
            print("Este alumno ya existe.")
        else:
            edad = int(input("Edad: "))
            curso = input("Curso: ")
            lenguajes_input = input("Lenguajes (separados por coma): ")
            lenguajes = {leng.strip() for leng in lenguajes_input.split(",")}
            nota = float(input("Nota: "))

            alumnos[nombre_nuevo] = {
                "edad": edad,
                "curso": curso,
                "lenguajes": lenguajes,
                "nota": nota,
            }
            print(f"Alumno {nombre_nuevo.capitalize()} añadido correctamente.")

    elif opcion == "4":
        print("\nPrograma Terminado\n")
        break

    else:
        print("\nOpción no válida. Inténtalo de nuevo.")


print("\n******** Parte 6 - Buscar Alumno ********\n")

nombre_buscar = input("Nombre del alumno a buscar: ").lower()
if nombre_buscar in alumnos:
    datos = alumnos[nombre_buscar]
    print(f"\nDatos de {nombre_buscar.capitalize()}:")
    print(f"Edad: {datos['edad']}")
    print(f"Curso: {datos['curso']}")
    print(f"Lenguajes: {', '.join(datos['lenguajes'])}")
    print(f"Nota: {datos['nota']}")
else:
    print("Alumno no encontrado.")


print("\n******** Parte 7 - Añadir Alumno ********\n")

nombre_nuevo = input("Nombre del nuevo alumno: ").lower()
if nombre_nuevo in alumnos:
    print("Este alumno ya existe.")
else:
    edad = int(input("Edad: "))
    curso = input("Curso: ")
    lenguajes_input = input("Lenguajes (separados por coma): ")
    lenguajes = {leng.strip() for leng in lenguajes_input.split(",")}
    nota = float(input("Nota: "))

    alumnos[nombre_nuevo] = {
        "edad": edad,
        "curso": curso,
        "lenguajes": lenguajes,
        "nota": nota,
    }
    print(f"Alumno {nombre_nuevo.capitalize()} añadido correctamente.")


print("\n******** Parte 8 - Uso de break ********\n")

while True:
    nombre_nuevo = input(
        "Introducte el nombre del alumno (o escribe 'salir' para cancelar): "
    ).lower()

    if nombre_nuevo == "salir":
        print("Operación cancelada. Saliendo...")
        break

    if nombre_nuevo in alumnos:
        print("Este alumno ya existe.")
    else:
        edad = int(input("Edad: "))
        curso = input("Curso: ")
        lenguajes_input = input("Lenguajes (separados por coma): ")
        lenguajes = {leng.strip() for leng in lenguajes_input.split(",")}
        nota = float(input("Nota: "))
        alumnos[nombre_nuevo] = {
            "edad": edad,
            "curso": curso,
            "lenguajes": lenguajes,
            "nota": nota,          
        }
        print(f"Alumno {nombre_nuevo.capitalize()} añadido correctamente.")
        break


print("\n******** Reto Final - Media de todas las notas ********\n")

if alumnos:
    suma_notas = sum(datos["nota"] for datos in alumnos.values())
    media_total = suma_notas / len(alumnos)
    print(f"La nota media de la clase es: {media_total:.2f}")
else:
    print("No hay alumnos para calcular la media.")
