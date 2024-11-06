def subasta_programacion_dinamica(A, B, ofertas):
    n = len(ofertas)
    dp = [0] * (A + 1)
    asignacion = [[0] * n for _ in range(A + 1)]

    for i in range(n):
        p, m, M = ofertas[i]
        for j in range(A, -1, -1):
            for k in range(m, min(M, j) + 1):
                if dp[j] < dp[j - k] + p * k:
                    dp[j] = dp[j - k] + p * k
                    asignacion[j] = asignacion[j - k][:]
                    asignacion[j][i] += k

    mejor_precio = dp[A]
   
    return mejor_precio, asignacion[A]