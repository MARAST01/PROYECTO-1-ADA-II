def fuerza_bruta(palabra1, palabra2, cursor1, cursor2, i, d, r, a, k): 
    # Caso base: cuando ambas palabras han sido procesadas completamente
    if cursor1 == len(palabra1) and cursor2 == len(palabra2):
        return 0, []

    # Caso base: cuando la primera palabra se ha terminado
    if cursor1 == len(palabra1):
        acciones = ["Insertar ({})-> {}".format(palabra2[k], i) for k in range(cursor2, len(palabra2))]
        return (len(palabra2) - cursor2) * i, acciones

    # Caso base: cuando la segunda palabra se ha terminado
    if cursor2 == len(palabra2):
        acciones = ["Borrar ({})-> {}".format(palabra1[k], d) for k in range(cursor1, len(palabra1))]
        return (len(palabra1) - cursor1) * d, acciones

    # Reemplazar, insertar y borrar, se calcula el costo mínimo de cada acción
    costo_reemplazar, acciones_reemplazar = fuerza_bruta(palabra1, palabra2, cursor1 + 1, cursor2 + 1, i, d, r, a, k)
    costo_insertar, acciones_insertar = fuerza_bruta(palabra1, palabra2, cursor1, cursor2 + 1, i, d, r, a, k)
    costo_borrar, acciones_borrar = fuerza_bruta(palabra1, palabra2, cursor1 + 1, cursor2, i, d, r, a, k)

    costo_reemplazar += r
    costo_insertar += i
    costo_borrar += d

    # Nueva opción: kill lo que queda de palabra1 y luego insertar lo que queda de palabra2
    costo_kill = (len(palabra1) - cursor1) * k + (len(palabra2) - cursor2) * i
    acciones_kill = ["kill ({}) -> {}".format(palabra1[k], k) for k in range(cursor1, len(palabra1))] + \
                    ["Insertar ({})-> {}".format(palabra2[k], i) for k in range(cursor2, len(palabra2))]

    # Si las letras son iguales, se decide si avanzar o reemplazar (ya que reemplazar también avanza)
    if palabra1[cursor1] == palabra2[cursor2]:
        # Decidir si avanzar o reemplazar cuando las letras son iguales
        if a <= r:
            costo, acciones = fuerza_bruta(palabra1, palabra2, cursor1 + 1, cursor2 + 1, i, d, r, a, k)
            return costo + a, ["Avanzar ({} == {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], a)] + acciones
        else:
            return costo_reemplazar, ["Reemplazar ({} -> {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], r)] + acciones_reemplazar

    # Seleccionar la acción con el costo mínimo
    if costo_reemplazar <= costo_insertar and costo_reemplazar <= costo_borrar and costo_reemplazar <= costo_kill:
        return costo_reemplazar, ["Reemplazar ({} -> {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], r)] + acciones_reemplazar
    elif costo_insertar <= costo_borrar and costo_insertar <= costo_kill:
        return costo_insertar, ["Insertar ({}) -> {}".format(palabra2[cursor2], i)] + acciones_insertar
    elif costo_borrar <= costo_kill:
        return costo_borrar, ["Borrar ({}) -> {}".format(palabra1[cursor1], d)] + acciones_borrar
    else:
        return costo_kill, acciones_kill
