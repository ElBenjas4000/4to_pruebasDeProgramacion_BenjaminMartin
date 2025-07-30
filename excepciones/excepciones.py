#Excepciones en Python

#MemoryError
try:
    lista = [0] * (10**10)

except MemoryError:
    print("No hay suficiente memoria disponible")


#ValueError
try:
    int("hola")

except ValueError:
    print("No se puede convertir a entero")


#TypeError
try:
    len(4)

except TypeError:
    print("No se puede obtener la longitud de un entero")


#KeyError
try:
    d = {"a": 1, "b":2}
    d["c"]

except KeyError:
    print("La clave no existe en el diccionario")


try:
    d = {"a": 1, "b":2}
    d["x"] += 1

except KeyError:
    print("La clave no existe en el diccionario")

#StopIteration
try:
    it = iter([])
    next(it)

except StopIteration:
    print("No hay mas elementos en la iteracion")


#FileNotFoundError
try:
    f = open("archivo_que_no_existe.txt")

except FileNotFoundError:
    print("El archivo no existe")


#Raise
try:
    raise NameError("La variable no esta definida")

except NameError:
    print("La variable no esta definida")
    
try:
    raise ValueError("El valor no es valido")

except ValueError:
    print("El valor no es valido")

