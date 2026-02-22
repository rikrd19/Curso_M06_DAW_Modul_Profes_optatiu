print("""
\n================================================================
MINI INVESTIGACIÓN: GETTERS Y SETTERS EN PYTHON
Investigacion Realizada por el Equipo: Ricardo Avila / Zhen Yang
================================================================\n
""")

class Pollo:
    def __init__(self, raza, peso):
        # Usamos el guion bajo (_) para indicar que el atributo es "privado"
        # Esto significa: "Por favor, no toques esto directamente"
        self._raza = raza
        self._peso = peso

    # --- MÉTODO GETTER ---
    # Sirve para LEER el valor de forma segura.
    def get_peso(self):
        return f"{self._peso} kg"

    # --- MÉTODO SETTER ---
    # Sirve para MODIFICAR el valor, pero aplicando REGLAS.
    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self._peso = nuevo_peso
            print(f"\t[Sistema]: Peso actualizado correctamente a {nuevo_peso} kg.\n")
        else:
            # Aquí está la utilidad real: evitamos datos absurdos
            print(f"\t[ERROR]: El peso {nuevo_peso} no es válido. Un pollo debe pesar más de 0.")

# --- PRUEBA DEL PROGRAMA (SIMULACIÓN VIDA REAL) ---

print("****** Iniciando granja de Ricardo y Zhen ******\n")
mi_pollo = Pollo("Sedosa", 2)

# 1. Intentamos consultar el peso usando el GETTER
print(f"Estado inicial: El pollo es de raza {mi_pollo._raza} y pesa {mi_pollo.get_peso()}.")

# 2. Intentamos cambiar el peso a un valor imposible usando el SETTER
print("\nIntentando poner un peso de -5 kg...")
mi_pollo.set_peso(-5) 

# 3. Ponemos un peso lógico
print("\nIntentando poner un peso de 3 kg...")
mi_pollo.set_peso(3)

# 4. Verificamos el resultado final
print(f"Resultado final: Ahora el pollo pesa {mi_pollo.get_peso()}.\n")


