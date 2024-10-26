def programacion_voraz(palabra1, palabra2, i, d, r, a, k):
    m = len(palabra1)
    t = len(palabra2)
     
    cursor1, cursor2 = 0, 0
    costo_total = 0
    acciones = []

    while cursor1 < m or cursor2 < t:
        # Si llegamos al final de palabra1 pero no de palabra2, inserta lo que falta
        if cursor1 == m:
            acciones.append("Insertar ({}) -> {}".format(palabra2[cursor2], i))
            costo_total += i
            cursor2 += 1
            continue

        # Si llegamos al final de palabra2 pero no de palabra1, borra lo que sobra o usa 'kill'
        if cursor2 == t:
            costo_borrar = (m - cursor1) * d
            if k < costo_borrar:
                acciones.append("Kill ({}) -> {}".format(palabra1[cursor1:], k))
                costo_total += k
                break
            else:
                acciones.append("Borrar ({}) -> {}".format(palabra1[cursor1], d))
                costo_total += d
                cursor1 += 1
            continue

        # Si los caracteres coinciden
        if palabra1[cursor1] == palabra2[cursor2]:
            acciones.append("Avanzar ({} == {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], a))
            costo_total += a
            cursor1 += 1
            cursor2 += 1

        # Si no coinciden, elegimos la operación más barata: reemplazar, borrar o insertar
        else:


            if r <= d and r <= i and r <= d + i:
                acciones.append("Reemplazar ({} -> {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], r))
                costo_total += r
                cursor1 += 1
                cursor2 += 1
            elif d + i <= r:  # Si la suma de borrar e insertar es menor que reemplazar
                acciones.append("Borrar ({}) -> {}".format(palabra1[cursor1], d))
                costo_total += d
                cursor1 += 1
                acciones.append("Insertar ({}) -> {}".format(palabra2[cursor2], i))
                costo_total += i
                cursor2 += 1
           
            else:
                acciones.append("Insertar ({}) -> {}".format(palabra2[cursor2], i))
                costo_total += i
                cursor2 += 1

    return costo_total, acciones