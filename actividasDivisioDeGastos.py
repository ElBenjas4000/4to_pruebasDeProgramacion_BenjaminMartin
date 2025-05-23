import os
def clear():
    os.system('cls')

clear()
print("""
    Calcular presupuestos de viaje
""")

presupuesto = float(input("Cual es tu presupuesto inicial del viaje: $"))
total_gastado = float(input("Cuanto gastaste hasta ahora: $"))
numero_dias = int(input("\nCuantos dias dura el viaje: "))
numero_dias_transcurrido = int(input("Cuantos dias llevas de viaje: "))

gasto_promedio = lambda tg, nd: tg / nd
balance_diario = lambda p, gp, ndt: p - (gp * ndt)

print(f"\nGasto premedio dario: ${gasto_promedio(total_gastado, numero_dias): .2f}")
print(f"Balance disponible por dia: ${balance_diario(presupuesto, gasto_promedio(total_gastado, numero_dias), numero_dias_transcurrido): .2f}")