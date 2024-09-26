# Función para calcular el costo mínimo de transformar palabra1 en palabra2
def programacion_dinamica(palabra1, palabra2, i, d, r, a, k):
    m = len(palabra1)
    t = len(palabra2)

    # Inicializamos una tabla DP de tamaño (m+1) x (t+1) para almacenar los costos
    dp = [[float('inf')] * (t + 1) for _ in range(m + 1)]

    # Caso base: costo de convertir una cadena vacía en otra
    dp[m][t] = 0  # Ambos vacíos, costo 0

    # Llenar la tabla desde el final hacia el inicio
    for cursor1 in range(m, -1, -1):
        for cursor2 in range(t, -1, -1):
            if cursor1 < m and cursor2 < t and palabra1[cursor1] == palabra2[cursor2]:
                dp[cursor1][cursor2] = min(dp[cursor1][cursor2], dp[cursor1 + 1][cursor2 + 1] + a)

            if cursor1 < m and cursor2 < t:
                dp[cursor1][cursor2] = min(dp[cursor1][cursor2], dp[cursor1 + 1][cursor2 + 1] + r)  # Reemplazar

            if cursor1 < m:
                dp[cursor1][cursor2] = min(dp[cursor1][cursor2], dp[cursor1 + 1][cursor2] + d)  # Borrar

            if cursor2 < t:
                dp[cursor1][cursor2] = min(dp[cursor1][cursor2], dp[cursor1][cursor2 + 1] + i)  # Insertar

            if cursor1 < m:
                dp[cursor1][cursor2] = min(dp[cursor1][cursor2], dp[cursor1][t] + k)  # Kill todo desde cursor

    return dp[0][0]

