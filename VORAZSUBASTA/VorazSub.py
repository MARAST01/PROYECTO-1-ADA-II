def subasta_voraz(A, B, ofertas):
    # Ordenar las ofertas por el precio que ofrece cada oferente, de mayor a menor
    ofertas.sort(key=lambda oferta: oferta[0], reverse=True)  # Ordenar por pi (precio por acción)

    asignacion = []  # Lista para almacenar cuántas acciones se asignan a cada oferente
    total_asignadas = 0  # Número de acciones asignadas

    # Iteramos sobre las ofertas
    for pi, mi, Mi in ofertas:
        # Determinar cuántas acciones podemos asignar a este oferente
        acciones_disponibles = A - total_asignadas  # Acciones que quedan por asignar
        if acciones_disponibles <= 0:
            break  # Si ya no hay acciones para asignar, terminamos

        # Asignamos las acciones que podemos, respetando el rango [mi, Mi]
        acciones_asignadas = min(Mi, max(mi, acciones_disponibles))  # Máximo que podemos asignar
        asignacion.append(acciones_asignadas)  # Guardar la asignación
        total_asignadas += acciones_asignadas  # Actualizamos el número total de acciones asignadas

    # Si sobran acciones, las compra el gobierno al precio B
    if total_asignadas < A:
        acciones_gobierno = A - total_asignadas
        asignacion.append(acciones_gobierno)
    else:
        acciones_gobierno = 0
        asignacion.append(acciones_gobierno)

    # Calcular el valor total (vr)
    vr = 0
    for i, (pi, mi, Mi) in enumerate(ofertas):
        vr += asignacion[i] * pi
    vr += acciones_gobierno * B  # Las acciones compradas por el gobierno

    print(f"Mejor asignación: {asignacion}")
    print(f"Valor recibido máximo (vr): {vr}")


