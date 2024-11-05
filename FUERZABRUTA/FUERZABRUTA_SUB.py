def fuerza_bruta_sub(A, B, ofertas):
    n = len(ofertas)
    mejor_valor = 0
    mejor_asignacion = []

    # Función recursiva para probar todas las combinaciones posibles
    def probar_combinaciones(asignacion_actual, indice, acciones_restantes):
        nonlocal mejor_valor, mejor_asignacion

        # Si hemos asignado todas las acciones o hemos considerado todos los oferentes
        if indice == n:
            valor_actual = sum(xi * pi for xi, (pi, mi, Mi) in zip(asignacion_actual, ofertas))
            acciones_sobrantes = acciones_restantes
            valor_actual += acciones_sobrantes * B

            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_asignacion = asignacion_actual + [acciones_sobrantes]
            return

        pi, mi, Mi = ofertas[indice]

        # Probar todas las cantidades posibles de acciones para el oferente actual
        for xi in range(mi, min(Mi, acciones_restantes) + 1):
            probar_combinaciones(asignacion_actual + [xi], indice + 1, acciones_restantes - xi)

    # Iniciar la recursión
    probar_combinaciones([], 0, A)

    return mejor_valor, mejor_asignacion