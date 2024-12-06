import sys
import os

# Añade la carpeta principal al Python Path
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_proyecto)

# Importa la función después de añadir la ruta
from VORAZ.terminal_voraz import programacion_voraz
import timeit
# Variables
i = 1
d = 2
r = 3
a = 2
k = 1

# Casos de prueba con mayor complejidad
palabra11 = "gatocris"        # Combinación compleja de letras
palabra12 = "lunatiko"        # Introduce cambios mayores

palabra21 = "anperrito"         # Cambios intermedios
palabra22 = "peflorear"         # Cambia más de un carácter por índice

palabra31 = "capiedras"         # Sufijo añadido
palabra32 = "doensillas"        # Prefijo añadido

palabra41 = "carreformado"       # Sufijo extendido
palabra42 = "delaventanas"       # Cambios en el prefijo

palabra51 = "camCamarerazo"      # Introduce sufijo grande
palabra52 = "alwMedicinate"      # Prefijo y sufijo modificados

palabra61 = "ifowMariposando"     # Agrega sufijo y cambia el centro
palabra62 = "nicoGuitarrezas"     # Variación similar

palabra71 = "JamasDificultades"    # Pluralización y sufijo añadido
palabra72 = "siemprCompletandote"   # Cambios importantes

palabra81 = "nosequeDependenciosa"   # Aumenta la longitud y cambia el significado
palabra82 = "siqueseAbsolutismo"     # Cambia completamente el sufijo

palabra91 = "hitlercarDesperdiciando"  # Cambio progresivo
palabra92 = "deleutiDesperdiciador"  # Cambia la forma verbal

palabra101 = "buenoporfinaDesorganizados" # Pluralización y longitud máxima
palabra102 = "casiquenoterDesorganizando" # Cambia verbo y sufijo

# Main
if __name__ == "__main__":
    with open("vz_terminal.txt", "w") as archivo:
        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra11, palabra12, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 1 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra21, palabra22, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 2 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra31, palabra32, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 3 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra41, palabra42, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 4 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra51, palabra52, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 5 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra61, palabra62, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 6 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra71, palabra72, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 7 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra81, palabra82, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 8 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra91, palabra92, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 9 terminada")

        archivo.write(f"{timeit.timeit(lambda: programacion_voraz(palabra101, palabra102, i, d, r, a, k), number=50)/50 * 1000}\n")
        print("prueba 10 terminada")

    print("pruebas terminadas")
