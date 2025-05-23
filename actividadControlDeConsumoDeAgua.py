import os

def clear():
    os.system('cls')

clear()

print("\n   Control de Consumo de agua\n")
while True:
    try:
        peso = int(input("Cual es tu peso actual: "))
        acitividad_diaria = str(input("Cuanto seria tu nivel de actividad(bajo, medio, alto): "))
        break
    except ValueError:
        print("Debe ingresar datos validos")
        clear()
