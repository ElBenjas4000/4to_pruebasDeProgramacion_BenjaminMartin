def calcular_gasto_promedio(total_gastado, numero_dias):
    return total_gastado / numero_dias

def calcular_balance(presupuesto, gasto_promedio):
    return presupuesto - gasto_promedio

precupuesto = float(input("Cual es tu presupuesto inicial del viaje: "))
total_gastado = float(input("Cuanto gastaste hasta ahora: "))
numero_dias = int(input("Cuantos dias dura el viaje: "))
numero_dias_transcurrido = int(input("Cuantos dias llevas de viaje: "))

gasto_promedio = calcular_gasto_promedio(precupuesto, numero_dias)
balance_diario = calcular_balance(precupuesto, gasto_promedio)

print(f"\nGasto premedio dario: ${gasto_promedio: .2f}")
print(f"Balance disponible por dia: ${balance_diario: .2f}")