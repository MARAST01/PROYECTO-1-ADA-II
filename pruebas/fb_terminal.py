import sys
import os

# Añade la carpeta principal al Python Path
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_proyecto)

# Importa la función después de añadir la ruta
from DINAMICA.InteligenteDinamica import programacion_dinamica
import timeit

#variables
i = 1
d = 2
r = 3 
a = 2
k = 1

palabra11 = "gato"        # 4 letras
palabra12 = "luna"        # 4 letras

palabra21 = "perro"       # 5 letras 
palabra22 = "flore"       # 5 letras

palabra31 = "piedra"      # 6 letras
palabra32 = "sillas"       # 6 letras

palabra41 = "reforma"     # 7 letras
palabra42 = "ventana"     # 7 letras

palabra51 = "Camarero"    # 8 letras 
palabra52 = "Medicina"     # 8 letras

palabra61 = "Mariposas"    # 9 letras
palabra62 = "Guitarras"      # 9 letras

palabra71 = "Dificultad"    # 10 letras
palabra72 = "Completado"    # 10 letras

palabra81 = "Dependencia"   # 11 letras
palabra82 = "Absolutista"  # 11 letras

palabra91 = "Desperdiciar"  # 12 letras
palabra92 = "Desperdicios"  # 12 letras

palabra101 = "Desorganizado"  # 13 letras
palabra102 = "Desorganizada" # 13 letras


# main
if __name__ == "__main__":
    # Lista para almacenar los tiempos de cada prueba
    with open("fb_terminal.txt", "w") as archivo:
        archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra11, palabra12, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 1 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra21, palabra22, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 2 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra31, palabra32, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 3 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra41, palabra42, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 4 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra51, palabra52, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 5 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra61, palabra62, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 6 terminada")

        #archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra71, palabra72, i, d, r, a, k), number=50)/50 * 1000}\n")
        #print("prueba 7 terminada")

        #archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra81, palabra82, i, d, r, a, k), number=50)/50 * 1000}\n")
        #print("prueba 8 terminada")

        #archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra91, palabra92, i, d, r, a, k), number=50)/50 * 1000}\n")
        #print("prueba 9 terminada")

        #archivo.write(f"{timeit.timeit(lambda: programacion_dinamica(palabra101, palabra102, i, d, r, a, k), number=50)/50 * 1000}\n")
        #print("prueba 10 terminada")

        print("pruebas terminadas")
