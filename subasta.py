# A =cantidad de acciones
# B = precio minimo por accion
# n = cantidad de subastadores
# pi= precio a pagar por accion
# mi= numero minimo de acciones a comprar
# Mi= numero maximo de acciones a comprar
from FUERZABRUTASUBASTA.FUERZABRUTA_SUB import fuerza_bruta_sub_aux
from DINAMICASUB.DinamicaSub import subasta_programacion_dinamica

def subasta():
    
    # crear un arreglo de subastadores
    ofertas = []
    A= int(input("Ingrese el numero de acciones a subastar: "))
    B = int(input("Ingrese el precio minimo por accion: "))
    n = int(input("Ingrese el numero de subastadores: "))
    for i in range(n):
        # si i es el ultimo subastador
        print ("Oferta del subastador", i+1)
        pi = int(input("Ingrese el precio a pagar por accion: "))
        mi = int(input("Ingrese el numero minimo de acciones a comprar: "))
        Mi = int(input("Ingrese el numero maximo de acciones a comprar: "))
        ofertas.append([pi, mi, Mi])
        
    
    print("1. Fuerza Bruta")
    print("2. Programacion Dinamica")
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        fuerza_bruta_sub_aux(A, B, ofertas)
    elif opcion == 2:
        subasta_programacion_dinamica(A, B, ofertas)
        
   
        

    