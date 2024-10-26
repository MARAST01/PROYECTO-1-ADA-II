# A =cantidad de acciones
# B = precio minimo por accion
# n = cantidad de subastadores
# pi= precio a pagar por accion
# mi= numero minimo de acciones a comprar
# Mi= numero maximo de acciones a comprar
from FUERZABRUTASUBASTA.FUERZABRUTA_SUB import fuerza_bruta_iterativa
from DINAMICASUB.DinamicaSub import subasta_programacion_dinamica
from VORAZSUBASTA.VorazSub import subasta_voraz
import time
import tkinter as tk

from tkinter import messagebox
entries_ofertas = []



def subastaVentana():
    def obtener_valores(): 
        try:
             A = int(entry_A.get())
             B = int(entry_B.get())
             n = int(entry_n.get())
            # Llamar a la función que abre la nueva ventana para ingresar ofertas
             abrir_ventana_ofertas(n, A, B, )
        except ValueError:
           messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    def abrir_ventana_ofertas(n, A, B):
        # Crear una nueva ventana
        ventana_ofertas = tk.Toplevel(root)
        ventana_ofertas.title("Ofertas")
        label = tk.Label(ventana_ofertas, text="Ingrese las ofertas, precio por accion, cantidad minima a comprar, cantidad maxima a comprar (separadas por coma):")
        # Crear etiquetas y campos de entrada para las ofertas
        for i in range(n):
            label = tk.Label(ventana_ofertas, text=f"Ofertador {i + 1}:")
            label.pack(pady=5)
            entry_oferta = tk.Entry(ventana_ofertas)
            entry_oferta.pack(pady=5)
            entries_ofertas.append(entry_oferta)
        # Botón para enviar las ofertas
        button_bruta = tk.Button(ventana_ofertas, text="Fuerza bruta", command=lambda: procesar_ofertas(A, B, n, 1))
        button_bruta.pack(pady=20)
        button_dinamica = tk.Button(ventana_ofertas, text="Programación dinámica", command=lambda: procesar_ofertas(A, B, n, 2))
        button_dinamica.pack(pady=20)
        button_voraz = tk.Button(ventana_ofertas, text="Programación voraz", command=lambda: procesar_ofertas(A, B, n, 3))
        button_voraz.pack(pady=20)
        
    def procesar_ofertas(A, B, n, opcion):
        ofertas = []
        try:
         for entry in entries_ofertas:
             # Obtener el texto de cada entrada y convertirlo a una tupla
             oferta_text = entry.get()
             precio, min_acciones, max_acciones = map(int, oferta_text.split(','))
             ofertas.append((precio, min_acciones, max_acciones))
         # Aquí puedes llamar a tu función de subasta_programacion_dinamica(A, B, ofertas)
         # Por ahora, solo mostramos las ofertas
         if opcion == 1:
             start_time = time.time()
             fuerza_bruta_iterativa(A, B, ofertas)
             end_time = time.time()
             print(f"Tiempo de ejecución de Fuerza Bruta: {end_time - start_time} segundos")
         elif opcion == 2:
             start_time = time.time()
             subasta_programacion_dinamica(A, B, ofertas)
             end_time = time.time()
             print(f"Tiempo de ejecución de Programación Dinámica: {end_time - start_time} segundos")
         elif opcion == 3:
             start_time = time.time()
             subasta_voraz(A, B, ofertas)
             end_time = time.time()
             print(f"Tiempo de ejecución de Programación Voraz: {end_time - start_time} segundos")
        except ValueError:
         messagebox.showerror("Error", "Por favor, ingresa ofertas válidas en el formato correcto.")

       
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Subasta")
    # Crear y posicionar etiquetas y entradas
    label_A = tk.Label(root, text="Ingrese total de acciones:")
    label_A.pack(pady=5)
    entry_A = tk.Entry(root)
    entry_A.pack(pady=5)
    label_B = tk.Label(root, text="Ingrese precio minimo de accion:")
    label_B.pack(pady=5)
    entry_B = tk.Entry(root)
    entry_B.pack(pady=5)
    label_n = tk.Label(root, text="Ingrese número de oferentes:")
    label_n.pack(pady=5)
    entry_n = tk.Entry(root)
    entry_n.pack(pady=5)
    # Botón para obtener los valores
    button_submit = tk.Button(root, text="Ingresar", command=obtener_valores)
    button_submit.pack(pady=20)
       # Iniciar el bucle principal de la interfaz
    
    root.mainloop()


