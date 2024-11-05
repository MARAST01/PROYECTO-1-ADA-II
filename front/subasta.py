# A =cantidad de acciones
# B = precio minimo por accion
# n = cantidad de subastadores
# pi= precio a pagar por accion
# mi= numero minimo de acciones a comprar
# Mi= numero maximo de acciones a comprar
from FUERZABRUTA.FUERZABRUTA_SUB import fuerza_bruta_sub
from DINAMICA.DinamicaSub import subasta_programacion_dinamica
from VORAZ.VorazSub import subasta_voraz
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
        label.pack(pady=5)
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
        contenedor_mostrar = tk.Frame(ventana_ofertas, bg='#8FD4F7', width=535, height=535)
        
        contenedor_mostrar.pack(pady=20)
        
        def procesar_ofertas(A, B, n, opcion):
            ofertas = []
            try:
             for entry in entries_ofertas:
                 # Obtener el texto de cada entrada y convertirlo a una tupla
                 oferta_text = entry.get()
                 precio, min_acciones, max_acciones = map(int, oferta_text.split(','))
                 ofertas.append((precio, min_acciones, max_acciones))
             # Aquí puedes llamar a tu función de subasta_programacion_dinamica(A, B, ofertas)
             limpiar_contenedor()            
             # Por ahora, solo mostramos las ofertas
             if opcion == 1:
                 
                 start_time = time.time()
                 vm, ma = fuerza_bruta_sub(A, B, ofertas)
                 
                 
                 labelvm = tk.Label(contenedor_mostrar, text=f"Valor máximo: {vm}")
                 labelvm.pack(pady=5)
                 labelma = tk.Label(contenedor_mostrar, text=f"Mejor asignación")
                 labelma.pack(pady=5) 
                 for i in range(len(ma)):
                     if i == (len(ma) -1):
                            labelma = tk.Label(contenedor_mostrar, text=f"Oferta del gobierno: {ma[i]}")
                            labelma.pack(pady=5)
                     else:
                         labelma = tk.Label(contenedor_mostrar, text=f"Ofertador {[i+1]}: {ma[i]}")
                         labelma.pack(pady=5)
                   
                 
                 
                 end_time = time.time()
                 labeltime = tk.Label(contenedor_mostrar, text=f"Tiempo de ejecución: {end_time - start_time} segundos")
                 labeltime.pack(pady=5)
                 
             elif opcion == 2:
                 
                 start_time = time.time()
                 vmdin, vadin = subasta_programacion_dinamica(A, B, ofertas)
                 
                 labelvm = tk.Label(contenedor_mostrar, text=f"Valor máximo: {vmdin}")
                 labelvm.pack(pady=5)
                 labelma = tk.Label(contenedor_mostrar, text=f"Mejor asignación")
                 labelma.pack(pady=5)
                 for i in range(len(vadin)):
                     if i == (len(vadin) -1):
                            labelma = tk.Label(contenedor_mostrar, text=f"Oferta del gobierno: {vadin[i]}")
                            labelma.pack(pady=5)
                     else:
                         labelma = tk.Label(contenedor_mostrar, text=f"Ofertador {[i+1]}: {vadin[i]}")
                         labelma.pack(pady=5)
                 end_time = time.time()
                 labeltime = tk.Label(contenedor_mostrar, text=f"Tiempo de ejecución: {end_time - start_time} segundos")
                 labeltime.pack(pady=5)
             elif opcion == 3:
                 
                 start_time = time.time()
                 vmvoraz, mavoraz =subasta_voraz(A, B, ofertas)
                 
                 labelvm = tk.Label(contenedor_mostrar, text=f"Valor máximo: {vmvoraz}")
                 labelvm.pack(pady=5)
                 labelma = tk.Label(contenedor_mostrar, text=f"Mejor asignación")
                 labelma.pack(pady=5)
                 for i in range(len(mavoraz)):
                     if i == (len(mavoraz) -1):
                            labelma = tk.Label(contenedor_mostrar, text=f"Oferta del gobierno: {mavoraz[i]}")
                            labelma.pack(pady=5)
                     else:
                         labelma = tk.Label(contenedor_mostrar, text=f"Ofertador {[i+1]}: {mavoraz[i]}")
                         labelma.pack(pady=5)              
                 end_time = time.time()
                 labeltime = tk.Label(contenedor_mostrar, text=f"Tiempo de ejecución: {end_time - start_time} segundos")
                 labeltime.pack(pady=5)
            except ValueError:
             messagebox.showerror("Error", "Por favor, ingresa ofertas válidas en el formato correcto.")
        def limpiar_contenedor():
            for widget in contenedor_mostrar.winfo_children():
                widget.destroy()
    
       
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


