
import subprocess

def ejecutador():
    
    print("Ejecutando pruebas fuerza bruta")
    subprocess.run(["python3", "pruebas/fb_subasta.py"])
    subprocess.run(["python3", "pruebas/fb_terminal.py"])
    print("Ejecutando pruebas dinamicas")
    subprocess.run(["python3", "pruebas/dp_subasta.py"])
    subprocess.run(["python3", "pruebas/dp_terminal.py"])
    print("Ejecutando pruebas voraz")
    subprocess.run(["python3", "pruebas/vz_subasta.py"])
    subprocess.run(["python3", "pruebas/vz_terminal.py"])

    
if __name__ == "__main__":
    ejecutador()