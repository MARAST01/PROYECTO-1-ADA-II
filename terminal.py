from DINAMICA.InteligenteDinamica import programacion_dinamica
from FUERZABRUTA.InteligenteBruta import fuerza_bruta
from vorazterminal.terminal_voraz import programacion_voraz
from front import pagina_principal
#####################################
#NO SE ESTA USANDO, PERO SE TOMO REFERENCIA DE AQUI, NO BORRAR HASTA QUE NO SEA NECESARIO
#####################################
# Costos
a = 1  # avanzar
d = 2  # borrar
r = 3  # reemplazar
i = 2  # insertar
k = 1  # matar




# Función delete (borrar un carácter)

palabra1 = "algorithm"
palabra2 = "altruistic"

def terminal():
    pagina_principal.ventana_principal()
    print("Elige el método de transformación:")
    print("1. Fuerza Bruta")
    print("2. Programación Dinámica")
    print("3. programacion voraz")
    
    # Leemos la opción elegida
    opcion = int(input("Ingresa la opción (1, 2, 3): "))
    
    if opcion == 1:
        costo, acciones = fuerza_bruta(palabra1,palabra2,0,0,i,d,r,a,k)

        print(f"El costo mínimo para transformar '{palabra1}' en '{palabra2}' es: {costo}")
        print("Acciones realizadas:", acciones)

    if opcion == 2:
        costo, acciones = programacion_dinamica(palabra1, palabra2, i,d,r,a,k)
        print(f"El costo mínimo para transformar '{palabra1}' en '{palabra2}' es: {costo}")
        print("Acciones realizadas:", acciones)
    if opcion == 3:
        costo, acciones = programacion_voraz(palabra1, palabra2, i,d,r,a,k)
        print(f"El costo mínimo para transformar '{palabra1}' en '{palabra2}' es: {costo}")
        print("Acciones realizadas:", acciones)
        
