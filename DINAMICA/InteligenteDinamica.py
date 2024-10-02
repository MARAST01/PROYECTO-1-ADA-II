# Función para calcular el costo mínimo de transformar palabra1 en palabra2
# y devolver también la secuencia de movimientos
def programacion_dinamica(palabra1, palabra2, i, d, r, a, k):
    m = len(palabra1)
    t = len(palabra2)

    # Inicializamos una tabla DP de tamaño (m+1) x (t+1) para almacenar los costos
    dp = [[float('inf')] * (t + 1) for _ in range(m + 1)]
    movimientos = [[[] for _ in range(t + 1)] for _ in range(m + 1)]

    # Caso base: cuando ambas cadenas están vacías, el costo es 0
    dp[m][t] = 0

    # Llenar la tabla desde el final hacia el inicio
    for cursor1 in range(m, -1, -1):
        for cursor2 in range(t, -1, -1):
            # Caso cuando ambas palabras están completas
            if cursor1 == m and cursor2 == t:
                continue

            # Caso base: cuando la primera palabra está vacía, solo se pueden hacer inserciones
            if cursor1 == m:
                dp[cursor1][cursor2] = (t - cursor2) * i
                movimientos[cursor1][cursor2] = ["Insertar ({}) -> {}".format(palabra2[j], i) for j in range(cursor2, t)]
                continue

            # Caso base: cuando la segunda palabra está vacía, solo se pueden hacer borrados o kill
            if cursor2 == t:
                costo_borrar = (m - cursor1) * d
                costo_kill = k
                if costo_kill < costo_borrar:
                    dp[cursor1][cursor2] = costo_kill
                    movimientos[cursor1][cursor2] = ["Kill ({}) -> {}".format(palabra1[cursor1:], k)]
                else:
                    dp[cursor1][cursor2] = costo_borrar
                    movimientos[cursor1][cursor2] = ["Borrar ({}) -> {}".format(palabra1[j], d) for j in range(cursor1, m)]
                continue

            # Opción de avanzar si los caracteres coinciden
            if palabra1[cursor1] == palabra2[cursor2]:
                if dp[cursor1 + 1][cursor2 + 1] + a < dp[cursor1][cursor2]:
                    dp[cursor1][cursor2] = dp[cursor1 + 1][cursor2 + 1] + a
                    movimientos[cursor1][cursor2] = ["Avanzar ({} == {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], a)] + movimientos[cursor1 + 1][cursor2 + 1]

            # Opción de reemplazar
            if dp[cursor1 + 1][cursor2 + 1] + r < dp[cursor1][cursor2]:
                dp[cursor1][cursor2] = dp[cursor1 + 1][cursor2 + 1] + r
                movimientos[cursor1][cursor2] = ["Reemplazar ({} -> {}) -> {}".format(palabra1[cursor1], palabra2[cursor2], r)] + movimientos[cursor1 + 1][cursor2 + 1]

            # Opción de borrar
            if dp[cursor1 + 1][cursor2] + d < dp[cursor1][cursor2]:
                dp[cursor1][cursor2] = dp[cursor1 + 1][cursor2] + d
                movimientos[cursor1][cursor2] = ["Borrar ({}) -> {}".format(palabra1[cursor1], d)] + movimientos[cursor1 + 1][cursor2]

            # Opción de insertar
            if dp[cursor1][cursor2 + 1] + i < dp[cursor1][cursor2]:
                dp[cursor1][cursor2] = dp[cursor1][cursor2 + 1] + i
                movimientos[cursor1][cursor2] = ["Insertar ({}) -> {}".format(palabra2[cursor2], i)] + movimientos[cursor1][cursor2 + 1]

            # Opción de kill (eliminar todo desde cursor1 hasta el final e insertar lo que queda de palabra2)
            costo_kill = k + (t - cursor2) * i
            if costo_kill < dp[cursor1][cursor2]:
                dp[cursor1][cursor2] = costo_kill
                movimientos[cursor1][cursor2] = ["Kill ({}) -> {}".format(palabra1[cursor1:], k)] + \
                    ["Insertar ({}) -> {}".format(palabra2[j], i) for j in range(cursor2, t)]

    return dp[0][0], movimientos[0][0]
