def subasta_programacion_dinamica(A, B, ofertas):
    n = len(ofertas)
    # Ordenar las ofertas por precio en orden descendente para priorizar las mejores
    ofertas.sort(reverse=True, key=lambda x: x[0])  # Ordenar por precio (pi)

    dp = [0] * (A + 1)  # Tabla unidimensional para el valor máximo
    asignacion = [[0] * (A + 1) for _ in range(n)]  # Para almacenar la asignación óptima por oferente

    # Caso base: El gobierno compra todas las acciones a precio B
    for a in range(A + 1):
        dp[a] = a * B

    # Rellenar la tabla DP
    for i in range(n):
        pi, mi, Mi = ofertas[i]

        # Hacemos la iteración en reversa
        for a in range(A, -1, -1):
            # Probar asignar entre mi y Mi acciones al oferente i
            for xi in range(mi, min(Mi, a) + 1):
                valor_actual = xi * pi + dp[a - xi]
                if valor_actual > dp[a]:
                    dp[a] = valor_actual
                    asignacion[i][a] = xi  # Guardamos la asignación óptima para el oferente i

    # Reconstruimos la asignación óptima
    mejor_asignacion = [0] * n
    acciones_restantes = A

    for i in range(n):
        xi = asignacion[i][acciones_restantes]
        mejor_asignacion[i] += xi
        acciones_restantes -= xi

    # Finalmente, asignamos las acciones restantes al gobierno
    mejor_asignacion.append(acciones_restantes)

    # El valor máximo que podemos obtener es dp[A]
    max_vr = dp[A]
    
    print("Valor máximo:", max_vr)
    print("Mejor asignación:", mejor_asignacion)