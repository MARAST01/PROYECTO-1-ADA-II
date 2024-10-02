from terminal import terminal
from subasta import subastaVentana

def menu():
        print("1. Terminal inteligente")
        print("2. Subasta")
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
                terminal()
        elif opcion == 2:
                subastaVentana()
                

        else:
                print("Opcion no valida")
                exit()
                
