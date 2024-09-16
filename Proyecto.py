#funcion caracteres a array
def caracteres_a_array(cadena):
    arreglo = [c for c in cadena]
    return arreglo

print(caracteres_a_array("Hola mundo"))

#funcion advance
def advance(cursor):
    cursor += 1
    return cursor,"a"

#funcion delete
def delete(cursor,arreglo):
    return arreglo.pop(cursor),"d"

#funcion replace
def replace(cursor,arreglo,caracter):
    arreglo[cursor] = caracter
    return arreglo,"r"

#funcion insert
def insert(cursor,arreglo,caracter):
    arreglo.insert(cursor,caracter)
    return arreglo,"i"

#funcion kill
def kill(cursor,arreglo):
    return arreglo[:cursor],"k"

 