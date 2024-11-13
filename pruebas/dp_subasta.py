import sys
import os

# Añade la carpeta principal al Python Path
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_proyecto)

# Importa la función después de añadir la ruta
from DINAMICA.DinamicaSub import subasta_programacion_dinamica
import timeit

# entrada 1
A1 = 100
B1 = 10
n1 = 3
params1 = [
    (10, 0, 100),
    (15, 10, 20),
    (25, 15, 30)
]

# entrada 2
A2 = 110
B2 = 10
n2 = 4
params2 = [
    (10, 0, 110),
    (15, 10, 22),
    (25, 15, 32),
    (35, 20, 42)
]

# entrada 3
A3 = 120
B3 = 10
n3 = 5
params3 = [
    (10, 0, 120),
    (15, 10, 24),
    (25, 15, 34),
    (35, 20, 44),
    (20, 5, 20)
]

# entrada 4
A4 = 130
B4 = 10
n4 = 6
params4 = [
    (10, 0, 130),
    (15, 10, 26),
    (25, 15, 38),
    (35, 20, 46),
    (20, 5, 22),
    (15, 30, 35)
]

# entrada 5
A5 = 130
B5 = 10
n5 = 7
params5 = [
    (10, 0, 130),
    (15, 10, 28),
    (25, 15, 40),
    (35, 20, 48),
    (20, 5, 24),
    (15, 30, 40),
    (50, 60, 70)
]

# entrada 6
A6 = 140
B6 = 10
n6 = 8
params6 = [
    (10, 0, 140),
    (15, 10, 30),
    (25, 15, 42),
    (35, 20, 50),
    (20, 5, 26),
    (15, 30, 42),
    (50, 60, 72),
    (30, 30, 38)
]

# entrada 7
A7 = 150
B7 = 10
n7 = 9
params7 = [
    (10, 0, 150),
    (15, 10, 32),
    (25, 15, 44),
    (35, 20, 52),
    (20, 5, 28),
    (15, 30, 44),
    (50, 60, 74),
    (30, 30, 40),
    (70, 15, 25)
]

# entrada 8
A8 = 160
B8 = 10
n8 = 10
params8 = [
    (10, 0, 160),
    (15, 10, 34),
    (25, 15, 46),
    (35, 20, 54),
    (20, 5, 30),
    (15, 30, 46),
    (50, 60, 76),
    (30, 30, 42),
    (70, 15, 27),
    (25, 50, 60)
]

# entrada 9
A9 = 170
B9 = 10
n9 = 10
params9 = [
    (10, 0, 170),
    (15, 10, 36),
    (25, 15, 48),
    (35, 20, 56),
    (20, 5, 32),
    (15, 30, 50),
    (50, 60, 78),
    (30, 30, 44),
    (70, 15, 29),
    (25, 50, 62),
    (80, 10, 20)
]

# main
if __name__ == "__main__":
    # Lista para almacenar los tiempos de cada prueba
    tiempos = []
    with open("dp_subasta.txt", "w") as archivo:
        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A1, B1, params1), number=50)/50 * 1000}\n")
        print("prueba 1 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A2, B2, params2), number=50)/50 * 1000}\n")
        print("prueba 2 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A3, B3, params3), number=50)/50 * 1000}\n")
        print("prueba 3 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A4, B4, params4), number=50)/50 * 1000}\n")
        print("prueba 4 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A5, B5, params5), number=50)/50 * 1000}\n")
        print("prueba 5 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A6, B6, params6), number=50)/50 * 1000}\n")
        print("prueba 6 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A7, B7, params7), number=50)/50 * 1000}\n")
        print("prueba 7 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A8, B8, params8), number=50)/50 * 1000}\n")
        print("prueba 8 terminada")

        archivo.write(f"{timeit.timeit(lambda: subasta_programacion_dinamica(A9, B9, params9), number=50)/50 * 1000}\n")
        print("prueba 9 terminada")

        print("pruebas terminadas")
