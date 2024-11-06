def fuerza_bruta_sub(A, B, n, ofertas):
    mejor_valor = 0
    mejor_asignacion = []
    
    # Ordenar las ofertas en función del precio por acción de mayor a menor
    ofertas = sorted(ofertas, key=lambda x: x[0], reverse=True)
    

    # Generar todas las combinaciones posibles de asignaciones
    def generar_asignaciones(indice, acciones_totales, asignacion_actual):
        nonlocal mejor_valor, mejor_asignacion

        # Si hemos procesado todas las ofertas
        if indice == n:
            # Calcular el valor actual
            valor_actual = sum(asignacion_actual[i] * ofertas[i][0] for i in range(n))
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_asignacion = asignacion_actual[:]
            return

        # Obtener la oferta actual
        precio, min_acciones, max_acciones = ofertas[indice]

        # Probar todas las cantidades de acciones desde min hasta max para la oferta actual
        for cantidad in range(min_acciones, max_acciones + 1):
            # Asegurarse de no exceder la cantidad total de acciones
            if acciones_totales + cantidad <= A:
                asignacion_actual[indice] = cantidad
                generar_asignaciones(indice + 1, acciones_totales + cantidad, asignacion_actual)

        # También considerar no asignar acciones a esta oferta
        asignacion_actual[indice] = 0
        generar_asignaciones(indice + 1, acciones_totales, asignacion_actual)

    # Inicializar la lista de asignaciones
    asignacion_inicial = [0] * n
    generar_asignaciones(0, 0, asignacion_inicial)

    return mejor_valor, mejor_asignacion
