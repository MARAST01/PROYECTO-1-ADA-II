#funcion caracteres a array
def caracteres_a_array(cadena):
    arreglo = [c for c in cadena]
    return arreglo

#print(caracteres_a_array("Hola mundo"))

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

#funcion ingenua
def ingenua(inicio,resultado):
    cursor = 0
    cadena1 = caracteres_a_array(inicio)
    cadena2 = caracteres_a_array(resultado)
    cadena1 = kill(cursor,cadena1)
    costo = " "
    def aux_ingenua (cadena1,cadena2, cursor,costo):
        if cadena1 == cadena2:
            return costo, cadena1
        else:
            cadena1,costo = insert(cursor,cadena1,cadena2[cursor])
    return aux_ingenua(cadena1,cadena2, cursor, costo)
print(ingenua ("Hola mundo","Hola mundo cruel"))
