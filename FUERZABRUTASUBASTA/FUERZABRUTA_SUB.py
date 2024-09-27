
def fuerza_bruta_iterativa(A, B, ofertas):
    n = len(ofertas)
    
    # Inicializamos una tabla para almacenar los resultados
    # dp[i][j] será el valor máximo que se puede obtener con i acciones y los primeros j oferentes
    dp = [[0] * (n + 1) for _ in range(A + 1)]
    
    # Inicializamos un array para rastrear la mejor asignación
    asignaciones = [[[] for _ in range(n + 1)] for _ in range(A + 1)]

    # Iteramos sobre cada oferente
    for j in range(1, n + 1):
        pi, mi, Mi = ofertas[j - 1]  # Ofertas es 0-indexado

        # Iteramos sobre la cantidad de acciones disponibles
        for i in range(A + 1):
            # Sin asignar acciones al oferente actual
            dp[i][j] = dp[i][j - 1]
            asignaciones[i][j] = asignaciones[i][j-1] + [0]

            # Probar asignar xi acciones al oferente actual
            for xi in range(mi, min(Mi, i) + 1):
                valor_actual = xi * pi + dp[i - xi][j - 1]
                
                # Si encontramos un mejor valor, actualizamos
                if valor_actual > dp[i][j]:
                    dp[i][j] = valor_actual
                    asignaciones[i][j] = asignaciones[i - xi][j - 1] + [xi]
   
    # Si sobran acciones, el gobierno compra a un precio B
    acciones_sobrantes = A - sum(asignaciones[A][n])
    if acciones_sobrantes > 0:
        dp[A][n] += acciones_sobrantes * B
        asignaciones[A][n].append(acciones_sobrantes)
    else:
        asignaciones[A][n].append(0)

    # El valor máximo se encuentra en dp[A][n]
    print("Valor máximo:", dp[A][n])
    print("Mejor asignación:", asignaciones[A][n])