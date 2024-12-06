
import subprocess

def ejecutador():
    
    
    print("Ejecutando pruebas dinamicas")
    subprocess.run(["python", "pruebas/dp_subasta.py"])
    subprocess.run(["python", "pruebas/dp_terminal.py"])
    print("Ejecutando pruebas voraz")
    subprocess.run(["python", "pruebas/vz_subasta.py"])
    subprocess.run(["python", "pruebas/vz_terminal.py"])
    print("Ejecutando pruebas fuerza bruta")
    subprocess.run(["python", "pruebas/fb_subasta.py"])
    subprocess.run(["python", "pruebas/fb_terminal.py"])
    
if __name__ == "__main__":
    ejecutador()