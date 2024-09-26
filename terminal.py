from DINAMICA.InteligenteDinamica import programacion_dinamica
from FUERZABRUTA.InteligenteBruta import caracteres_a_array
from FUERZABRUTA.InteligenteBruta import fuerza_bruta

# Costos
a = 3  # avanzar
d = 2  # borrar
r = 1  # reemplazar
i = 2  # insertar
k = 3  # eliminar en adelante


# Función delete (borrar un carácter)


palabra1 = "ingeniero"
palabra2 = "ingenioso"

def terminal():
    print("Elige el método de transformación:")
    print("1. Fuerza Bruta")
    print("2. Programación Dinámica")
    
    # Leemos la opción elegida
    opcion = int(input("Ingresa la opción (1 o 2): "))
    
    if opcion == 1:
        costo_minimo = fuerza_bruta(palabra1, palabra2, caracteres_a_array,i,d,r,a,k)
        print(f"El costo mínimo para transformar '{palabra1}' en '{palabra2}' es: {costo_minimo}")

    if opcion == 2:
        costo_minimo = programacion_dinamica(palabra1, palabra2, i,d,r,a,k)
        print(f"El costo mínimo para transformar '{palabra1}' en '{palabra2}' es: {costo_minimo}")


