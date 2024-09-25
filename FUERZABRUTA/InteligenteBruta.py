#from main import delete, replace, insertar, kill
def caracteres_a_array(cadena):
        return [c for c in cadena]
    
def fuerza_bruta(palabra1, palabra2, caracteres_a_array):
    

    palabra1 = caracteres_a_array(palabra1)
    palabra2 = caracteres_a_array(palabra2)
    
    # Función recursiva para encontrar el costo mínimo
    def aux_bruto(palabra1, palabra2, cursor1, cursor2, costo):
        # Caso base: si ambas palabras se han procesado completamente
        if cursor1 == len(palabra1) and cursor2 == len(palabra2):
            return costo  # Ambas palabras se han procesado completamente

        # Si palabra1 se terminó pero palabra2 no, hay que insertar lo que falta
        if cursor1 == len(palabra1):
            return costo + i * (len(palabra2) - cursor2)  # Insertar caracteres restantes

        # Si palabra2 se terminó pero palabra1 no, hay que borrar lo que sobra
        if cursor2 == len(palabra2):
            return costo + d * (len(palabra1) - cursor1)  # Borrar caracteres restantes

        # Casos recursivos: evaluar todas las operaciones posibles en cada paso

        # Opción 1: Insertar un carácter en palabra1
        palabrai = insertar(cursor1, palabra1, palabra2[cursor2])
        costo_insertar = aux_bruto(palabrai, palabra2, cursor1 + 1, cursor2 + 1, costo + i)

        # Opción 2: Borrar un carácter de palabra1
        palabrad = delete(cursor1, palabra1)
        costo_borrar = aux_bruto(palabrad, palabra2, cursor1, cursor2, costo + d)

        # Opción 3: Reemplazar un carácter en palabra1
        palabrar = replace(cursor1, palabra1, palabra2[cursor2])
        costo_reemplazar = aux_bruto(palabrar, palabra2, cursor1 + 1, cursor2 + 1, costo + r)

        # Opción 4: Eliminar todo desde el cursor en palabra1
        palabrak = kill(cursor1, palabra1)
        costo_kill = aux_bruto(palabrak, palabra2, cursor1, cursor2, costo + k)

        # Opción 5: Avanzar si los caracteres son iguales
        if palabra1[cursor1] == palabra2[cursor2]:
            costo_avanzar = aux_bruto(palabra1, palabra2, cursor1 + 1, cursor2 + 1, costo + a)
            return min(costo_insertar, costo_borrar, costo_reemplazar, costo_kill, costo_avanzar)
        else:
            return min(costo_insertar, costo_borrar, costo_reemplazar, costo_kill)

    # Llamar a la función recursiva inicial
    return aux_bruto(palabra1, palabra2, 0, 0, 0)

