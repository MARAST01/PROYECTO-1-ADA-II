from terminal import terminal
from subasta import subasta


print("1. Terminal inteligente")
print("2. Subasta")
opcion = int(input("Elija una opcion: "))
if opcion == 1:
        terminal()
elif opcion == 2:
        subasta()