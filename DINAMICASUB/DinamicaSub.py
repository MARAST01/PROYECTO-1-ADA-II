def subasta_programacion_dinamica(A, B, ofertas):
    # Crear una tabla de DP, donde dp[i][a] representa el valor máximo para los oferentes i...n con a acciones
    n = len(ofertas)
    dp = [[-1] * (A + 1) for _ in range(n + 1)]  # Inicializamos con -1 para indicar que no ha sido calculado
    asignacion = [[None] * (A + 1) for _ in range(n + 1)]  # Para almacenar las asignaciones óptimas

    # Caso base: Si no hay oferentes restantes, el gobierno compra todas las acciones
    for a in range(A + 1):
        dp[n][a] = a * B  # El gobierno compra a precio B

    # Rellenar la tabla DP de abajo hacia arriba
    for i in range(n - 1, -1, -1):  # Recorremos los oferentes
        pi, mi, Mi = ofertas[i]  # Obtenemos los datos del oferente actual
        for a in range(A + 1):  # Recorremos el número de acciones restantes
            # Intentamos asignar entre mi y Mi acciones al oferente i
            dp[i][a] = -float('inf')  # Inicializamos con un valor muy bajo
            for xi in range(mi, min(Mi, a) + 1):  # Asignamos xi acciones al oferente i
                valor_actual = xi * pi + dp[i + 1][a - xi]
                if valor_actual > dp[i][a]:
                    dp[i][a] = valor_actual
                    asignacion[i][a] = xi  # Guardamos la asignación óptima

    # Reconstruimos la asignación óptima
    mejor_asignacion = []
    acciones_restantes = A
    for i in range(n):
        xi = asignacion[i][acciones_restantes]
        mejor_asignacion.append(xi)
        acciones_restantes -= xi

    # Finalmente, asignamos las acciones restantes al gobierno
    mejor_asignacion.append(acciones_restantes)

    # El valor máximo que podemos obtener es dp[0][A]
    max_vr = dp[0][A]
    
    print(max_vr)
    print(mejor_asignacion)