print("------ ejercicio 1 - Condicion simple (if) ------ n")
print("\t EMPRESA NexoraTech \n\n")

numero_horas_trabajadas = 20

if numero_horas_trabajadas > 0:
    print(f"Las horas fueron registradas correctamente: {numero_horas_trabajadas} horas trabajadas ")
else:
    print("Las horas no se registraron correctamente")



print("\n------ ejercicio 2 - Uso de if y else ------\n")

hora_llegada_empleado = 9

if hora_llegada_empleado <= 8:
    print("¡Llegaste a tiempo!")
else:
    print("Llegada tarde, fuera de la hora pautada.")

print("\n------ ejercicio 3 - Operadores logicos (and) ------\n")

horas_trabajadas_diarias = 8

if horas_trabajadas_diarias >= 0 and horas_trabajadas_diarias <= 12:
    print(f"Horas registradas correctamente: {horas_trabajadas_diarias} horas")
else:
    print("Error: El número de horas debe estar entre 0 y 12 horas")



print("\n------ ejercicio 4 - Uso de elif ------\n")


minutos_de_retraso = 10

if minutos_de_retraso == 0:
    print("llegada puntual. Excelente !")
elif minutos_de_retraso <= 5:
    print("Retraso menor. Se ha registrado")
elif minutos_de_retraso <= 15:
    print("Retraso moderado. Recibirás una amonestación!")
else:
    print("Retraso mayor. Debes justificar tu llegada tarde")

print("\n------ ejercicio 5 - String en condicionales ------\n")

motivo_de_ausencia = "Cita médica"

if motivo_de_ausencia:
    print(f"Motivo de ausencia registrado: {motivo_de_ausencia}")
else:
    print("El motivo de la ausencia no ha sido registrado.")



print("\n------ ejercicio 6 - Uso de not ------\n")

hora_de_salida = ""

if not hora_de_salida:
    print("Aviso: No se ha registrado la hora de salida.")
else:
    print(f"Hora de salida registrada: {hora_de_salida}")