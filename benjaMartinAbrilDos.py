import os

def clear():
    os.system('cls')

def CantidadTareas(cant_de_tareas):
    diccionario_de_tareas = {}

    for i in range(len(cant_de_tareas)):
        diccionario_de_tareas[i+1] = cant_de_tareas[i]

    for nuemro, tarea in diccionario_de_tareas.items():
        print(f"{nuemro}. ", tarea)

cantidad_de_tareas = []

while True:
    clear()
    print("Gestion de tareas")
    print()
    print("1. Añadir una terea")
    print(f"2. Ver todas las Tareas (en total son {len(cantidad_de_tareas)})")
    print("3. Marcar una tarea como completa")
    print("4. Salir")

    while True:
        try:
            accion = int(input("Ingrese el numero de lo que quiere hacer:  "))
            break
        except:
            print("Tiene que ingresar un numero")

    
    if accion == 1:
        print("Que tarea desea agregar")
        tarea = str(input(">> "))
        cantidad_de_tareas.append(tarea)
        continue

    elif accion == 2:
        clear()
        CantidadTareas(cantidad_de_tareas)

        while True:
            try:
                volver = int(input("Ingrese 1 para volver:  "))
                break
            except:
                print("Tiene que ingresar un numero")

    elif accion == 3:
        clear()
        CantidadTareas(cantidad_de_tareas)
        print("¿Qué numero de tarea quiere borrar?")
        tarea_para_eliminar = int(input(">> "))
        cantidad_de_tareas.pop(tarea_para_eliminar - 1)
        while True:
            try:
                volver = int(input("Ingrese 1 para volver:  "))
                break
            except:
                print("Tiene que ingresar un numero")

    elif accion == 4:
        break

print("Espero que cumplas tus tareas. Nos vemos")
