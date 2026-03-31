
# examen optativa DAW

# Ricard Avila

print("\n======== EXAMEN PYTHON =========")
print("================================")
"""
crear un programa para gestionar alumnos y sus cursos en un centro (registro sencillo). el programa 
tendra un menu que permita anadir alumnos, matricularlos en cursos, consultar fichas , 
listar alumnos , mostrar estadisticas y salir.

a) Cada alumno tendra un set de cursos matriculados no se permiten repetidos.
b) set obligatorio.
c) diccionario obligatorio.
d) condicionales  + bucles obligatorios.
e) funciones obligatorias.
f) clases obligatorias.
g) excepciones obligatorias.
"""

alumnos = {}

# a) TUPLA cursos disponibles (Obligatorio)
CURSOS_DISPONIBLES = (
    "python",
    "java",
    "react",
    "html",
    "css"
)

# f) Clase Alumno (Obligatorio)
# Define la estructura de cada estudiante
class Alumno:
    # Constructor de la clase
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        # b) Set (Obligatorio) para evitar cursos duplicados
        self.cursos = set()

    # Método para añadir un curso al conjunto (set)
    def matricular(self, curso):
        # Al ser un set, si el curso ya está, pyhon lo ignora.
        self.cursos.add(curso)

    # Método para definir cómo se muestra el alumno usando print()
    def __str__(self):
        # Si el set NO tiene cursos, mostramos (sin cursos)
        if not self.cursos:
            texto_cursos = "(sin cursos)"
        else:
            # Unimos los elementos del set separados por coma
            texto_cursos = ", ".join(self.cursos)
            
        return f"{self.dni} - {self.nombre} - Edad: {self.edad} - Cursos: {texto_cursos}"


# e) Funciones (Obligatorias)

# Función 1: Muestra el menú por pantalla
def mostrar_menu():
    print("""
    \n-- Ingresa una opción --
    1. Añadir alumno
    2. Matricular alumno en curso
    3. Mostrar ficha de un alumno
    4. Listar alumnos 
    5. Estadísticas
    6. Salir
    """)

# Función 2: Pide una opción y verifica que sea un número válido
# g) Excepciones (Obligatorio): controlamos el int(input())
def pedir_opcion():
    while True:
        try:
            opcion = int(input("\n-> Elige una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("\nX  Opción fuera de rango. Elige entre 1 y 6.")
        except ValueError:
            print("\nX  Entrada inválida. Debes escribir un número entero.")

# Función 3: Pide y valida la edad usando excepciones
def pedir_edad():
    while True:
        try:
            edad = int(input("Introduce la edad: "))
            if edad > 0:
                return edad
            else:
                print("\nX  La edad debe ser mayor que 0.")
        # g) Excepciones (Obligatorio)
        except ValueError:
            print("\nX  Edad invalida, debes escribir un numero")

# Función 4: Pide un DNI asegurando que no esté vacío
def pedir_dni():
    while True:
        dni = input("Introduce el DNI: ").strip()
        if dni == "":
            print("X El DNI no puede estar vacío.")
        else:
            return dni


# --- PROGRAMA PRINCIPAL ---

print("\n=========================================")
print("========== Menu interactivo =============")  
print("=========================================")

# d) Condicionales + bucles (Obligatorio)
while True:
    mostrar_menu()
    opcion = pedir_opcion()

    # OPCIÓN 1: Añadir alumno
    if opcion == 1:
        print("\n--- Añadir alumno ---")
        dni = pedir_dni()
        
        # Comprobamos si el DNI ya está en el diccionario de alumnos
        if dni in alumnos:
            print(f"X Ya existe un alumno con el DNI '{dni}'")
        else:
            # Pedimos nombre validando que no esté vacío
            while True:
                nombre = input("Introduce el nombre del alumno: ").strip()
                if nombre != "":
                    break
                print("X El nombre no puede estar vacío.")
                
            edad = pedir_edad()
            
            # Instanciamos el objeto de la clase Alumno
            nuevo_alumno = Alumno(dni, nombre, edad)
            
            # c) Diccionarios (Obligatorio): clave DNI, valor Objeto Alumno
            alumnos[dni] = nuevo_alumno
            print("\n  √  alumno añadido")

    # OPCIÓN 2: Matricular alumno en curso
    # Se matricula si en el paso 1 se agrego Alumno
    elif opcion == 2:
        print("\n--- Matricular alumno en curso si previamente fue agregado ---")
        dni = pedir_dni()
        
        # Validamos si existe en nuestro diccionario
        if dni not in alumnos:
            print("X Alumno no encontrado")
        else:
            curso = input("Introduce el curso (en minúsculas): ").strip().lower()
            
            # Validamos si el curso existe en la tupla
            if curso not in CURSOS_DISPONIBLES:
                print("X Curso Invalido")
            else:
                # Accedemos al objeto alumno mediante su DNI y llamamos a matricular
                alumno_actual = alumnos[dni]
                alumno_actual.matricular(curso)
                print("√ curso matriculado")

    # OPCIÓN 3: Mostrar ficha de un alumno
    elif opcion == 3:
        print("\n--- Mostrar ficha de un alumno ---")
        dni = pedir_dni()
        
        if dni in alumnos:
            # Al hacer print() de un objeto Alumno, se ejecuta su método __str__
            print("Ficha:", alumnos[dni])
        else:
            print("X Alumno no encontrado")

    # OPCIÓN 4: Listar alumnos
    elif opcion == 4:
        print("\n--- Listar alumnos (Resumen) ---")
        if len(alumnos) == 0:
            print("No hay alumnos registrados.")
        else:
            # Iteramos sobre los valores del diccionario (los objetos Alumno)
            for alumno in alumnos.values():
                # Obtenemos la longitud del set (número de cursos matriculados)
                num_cursos = len(alumno.cursos)
                print(f"{alumno.dni} - {alumno.nombre} - Cursos matriculados: {num_cursos}")

    # OPCIÓN 5: Estadísticas
    elif opcion == 5:
        print("\n--- Estadísticas ---")
        total_alumnos = len(alumnos)
        print(f"Total alumnos: {total_alumnos}")
        
        total_cursos_disp = len(CURSOS_DISPONIBLES)
        print(f"Total cursos disponibles: {total_cursos_disp}")
        
        if total_alumnos > 0:
            # Calculamos el curso más repetido usando un diccionario contador
            # Pista del enunciado: clave=curso, valor=cantidad
            contador_cursos = {}
            for alumno in alumnos.values():
                for curso in alumno.cursos:
                    # Si el curso ya está en el contador, le sumamos 1, si no, lo inicializamos a 1.
                    # El método get() devuelve 0 si no existe la clave.
                    contador_cursos[curso] = contador_cursos.get(curso, 0) + 1
            
            if len(contador_cursos) > 0:
                # Buscamos la clave (curso) con el valor (cantidad) más alto
                curso_mas_repetido = max(contador_cursos, key=contador_cursos.get)
                cantidad_maxima = contador_cursos[curso_mas_repetido]
                print(f"Curso más repetido: {curso_mas_repetido} ({cantidad_maxima} alumnos matriculados)")
            else:
                print("Curso más repetido: Nadie se ha matriculado en ningún curso aún.")
        else:
            print("Curso más repetido: No hay alumnos registrados.")

    # OPCIÓN 6: Salir
    elif opcion == 6:
        print("\n ¡Programa finalizado, hasta luego! ---")
        break


    