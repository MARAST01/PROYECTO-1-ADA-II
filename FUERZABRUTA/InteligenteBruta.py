def fuerza_bruta(palabra1, palabra2, cursor1, cursor2, i, d, r, a, k): 
    # Caso base: cuando ambas palabras han sido procesadas completamente
    if cursor1 == len(palabra1) and cursor2 == len(palabra2):
        return 0, []
    
    # Caso base: cuando  la primera palabra se ha terminado
    if cursor1 == len(palabra1):
        acciones = ["Insertar ({})-> {}".format(palabra2[j], i) for j in range(cursor2, len(palabra2))]
        return (len(palabra2) - cursor2) * i, acciones
    
    # Caso base: cuando la segunda palabra se ha terminado
    # Caso base: cuando la segunda palabra se ha terminado
    if cursor2 == len(palabra2):
        # Costo de borrar cada letra desde cursor1 hasta el final
        costo_borrar = (len(palabra1) - cursor1) * d
        acciones_borrar = ["Borrar ({})-> {}".format(palabra1[j], d) for j in range(cursor1, len(palabra1))]
    
        # Costo de la operación kill
        costo_kill = k
        acciones_kill = ["Kill ({}) -> {}".format(palabra1[cursor1:], k)]
    
        # Comparar costos y elegir la acción más barata
        if costo_kill < costo_borrar:
            return costo_kill, acciones_kill
        else:
            return costo_borrar, acciones_borrar

    
    # Reemplazar, insertar y borrar, se calcula el costo mínimo de cada acción
    costo_reemplazar, acciones_reemplazar = fuerza_bruta(palabra1, palabra2, cursor1 + 1, cursor2 + 1, i, d, r, a, k)
    costo_insertar, acciones_insertar = fuerza_bruta(palabra1, palabra2, cursor1, cursor2 + 1, i, d, r, a, k)
    costo_borrar, acciones_borrar = fuerza_bruta(palabra1, palabra2, cursor1 + 1, cursor2, i, d, r, a, k)
    
    costo_reemplazar += r
    costo_insertar += i
    costo_borrar += d

    # Opción de 'kill': elimina todo lo que queda de palabra1 y luego inserta lo que queda de palabra2
    costo_kill = (len(palabra1) - cursor1) * k + (len(palabra2) - cursor2) * i
    acciones_kill = ["Kill ({}) -> {}".format(palabra1[j], k) for j in range(cursor1, len(palabra1))] + \
                    ["Insertar ({})-> {}".format(palabra2[j], i) for j in range(cursor2, len(palabra2))]

    # Si las letras son iguales, decidir si avanzar o reemplazar
    if palabra1[cursor1] == palabra2[cursor2]:
        costo_avanzar, acciones_avanzar = fuerza_bruta(palabra1, palabra2, cursor1 + 1, cursor2 + 1, i, d, r, a, k)
        costo_avanzar += a
        # Comparar costos y elegir la acción más barata
        opciones = [(costo_reemplazar, acciones_reemplazar, "Reemplazar ({} -> {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], r)),
                (costo_insertar, acciones_insertar, "Insertar ({}) -> {}".format(palabra2[cursor2], i)),
                (costo_borrar, acciones_borrar, "Borrar ({}) -> {}".format(palabra1[cursor1], d)),
                (costo_kill, acciones_kill, "Kill ({}) -> {}".format(palabra1[cursor1], k)),
                (costo_avanzar, acciones_avanzar, "Avanzar ({} == {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], a))]
        
        costo_minimo, acciones_minimas, accion = min(opciones, key=lambda x: x[0])
        return costo_minimo, [accion] + acciones_minimas       
    # comparar costos sin avanzar
    opciones = [(costo_reemplazar, acciones_reemplazar, "Reemplazar ({} -> {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], r)),
                (costo_insertar, acciones_insertar, "Insertar ({}) -> {}".format(palabra2[cursor2], i)),
                (costo_borrar, acciones_borrar, "Borrar ({}) -> {}".format(palabra1[cursor1], d)),
                (costo_kill, acciones_kill, "Kill ({}) -> {}".format(palabra1[cursor1], k))]

    # Seleccionar la acción con el costo mínimo
    costo_minimo, acciones_minimas, accion = min(opciones, key=lambda x: x[0])
    return costo_minimo, [accion] + acciones_minimas


a = 5  # avanzar
d = 5  # borrar
r = 5  # reemplazar
i = 1  # insertar
k = 1  # matar



# Función delete (borrar un carácter)

palabra1 = "aaa"
palabra2 = "aaa"
costo, acciones = fuerza_bruta(palabra1,palabra2,0,0,i,d,r,a,k)
#imprimir costo y acciones
print(f"El costo mínimo para transformar '{palabra1}' en '{palabra2}' es: {costo}")
print("Acciones realizadas:", acciones)