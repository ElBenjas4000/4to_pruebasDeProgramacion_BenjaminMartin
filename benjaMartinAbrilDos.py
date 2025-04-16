import os

def clear():
    os.system('cls')

def CantidadTareas(cant_de_tareas):
    diccionario_de_tareas = {}
    for i in range(len(cant_de_tareas)):
        diccionario_de_tareas.update(f"{i+1}. ", cant_de_tareas[i])
    return diccionario_de_tareas

cantidad_de_tareas = ["Acomodar la cama", "Cocinar", "Lavar la ropa"]

CantidadTareas(cantidad_de_tareas)