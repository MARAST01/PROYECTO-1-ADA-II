
from FUERZABRUTA.FUERZABRUTA_SUB import fuerza_bruta_sub
from DINAMICA.DinamicaSub import subasta_programacion_dinamica
from VORAZ.VorazSub import subasta_voraz
import time
import tkinter as tk
from tkinter import PhotoImage, font  
import os
from tkinter import messagebox
entries_ofertas = []
iconos_dir = os.path.join(os.path.dirname(__file__), 'ICONOS')


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
        ventana_ofertas.title("OFERTAS")
        ventana_ofertas.geometry("600x750")  # Ajuste de altura para ver más contenido con scroll
        ventana_ofertas.configure(bg='#6fa1e4')
        
        # ──── ✧《CANVAS CON SCROLL PARA TODA LA VENTANA》✧ ──── #
        canvas = tk.Canvas(ventana_ofertas, bg='#6fa1e4')
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(ventana_ofertas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

      # Frame contenedor dentro del canvas centrado
        ContenedorPrincipal = tk.Frame(canvas, bg='#6fa1e4')
        ContenedorPrincipal_id = canvas.create_window((0, 0), window=ContenedorPrincipal, anchor="n")

# Configurar el scroll y centrar el contenido horizontalmente cuando se cambie el tamaño
        def update_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(ContenedorPrincipal_id, width=canvas.winfo_width())

        ContenedorPrincipal.bind("<Configure>", update_scroll_region)
        ventana_ofertas.bind("<Configure>", update_scroll_region)   

        # ──── ✧《FUENTE E ICONOS》✧ ──── #
        

        custom_font_title = font.Font(family="Times New Roman", size=30, weight="bold")
        custom_font_texto = font.Font(family="Times New Roman", size=20, weight="bold")
        custom_font_button = font.Font(family="Times New Romans", size=10, weight="bold")
        custom_font_info = font.Font(family="Times New Roman", size=9, weight="bold")

        
        
        # Cargar iconos
        subasta = PhotoImage(file=os.path.join(iconos_dir, 'subasta.png'))
         # Icono de solución dinámica
        # ──── ✧《TITULO》✧ ──── #
        tk.Label(ContenedorPrincipal, text="OFERTAS", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_title).pack(pady=(10, 0))

        # CONTENIDO DEL CONTENEDOR MENU
        labelInfo = tk.Label(ContenedorPrincipal, text="Ingrese las ofertas, precio por acción, cantidad mínima a comprar, \n cantidad máxima a comprar (separadas por coma).", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_info).pack(pady=(10, 0))

        # Subcontenedor para los campos de entrada
        subcontenedor = tk.Frame(ContenedorPrincipal, bg='#8FD4F7', width=535, height=830, bd=5, relief='ridge')
        subcontenedor.pack(pady=20)
        subcontenedor.pack_propagate(False)
        
        # label = tk.Label(ventana_ofertas, text="Ingrese las ofertas, precio por accion, cantidad minima a comprar, cantidad maxima a comprar (separadas por coma):")
        # label.pack(pady=5)
        # Crear etiquetas y campos de entrada para las ofertas
        for i in range(n):
            # label = tk.Label(ventana_ofertas, text=f"Ofertador {i + 1}:")
            # label.pack(pady=5)
            # entry_oferta = tk.Entry(ventana_ofertas)
            # entry_oferta.pack(pady=5)
            # entries_ofertas.append(entry_oferta)
            
            label_A = tk.Label(subcontenedor, text=f"OFERTADOR {i+1}", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_texto).pack(pady=(10, 0))
            entry_oferta = tk.Entry(subcontenedor, width=23, font=('Arial', 14))
            entry_oferta.pack(pady=(0, 10))
            entries_ofertas.append(entry_oferta)
        
        label = tk.Label(subcontenedor, text="OFERTA DEL GOBIERNO",fg='#6fa1e4', bg='#8FD4F7', font=custom_font_texto).pack(pady=(10, 0))
        entry_oferta = tk.Entry(subcontenedor, width=23, font=('Arial', 14))
        entry_oferta.insert(0, f"{B},0,{A}")
        entry_oferta.config(state='readonly')
        entry_oferta.pack(pady=(0, 10))
        entries_ofertas.append(entry_oferta)
        
        
                # ──── ✧《BOTONES DE SOLUCIÓN》✧ ──── #
        # Contenedor: botones de soluciones y colocarlos en fila
        frame_botones_soluciones = tk.Frame(subcontenedor, bg='#8FD4F7')
        frame_botones_soluciones.pack(pady=(10, 0))

        # Boton solución ingenua
        btn_sol_ingenua = tk.Button(frame_botones_soluciones, text="SOLUCIÓN INGENUA", fg='#ffe1f5', bg='#F1A7F1', font=custom_font_button, image=icono_sol_ingenua, compound='top', width=140, height=100,command=lambda: procesar_ofertas(A, B, n, 1))
        btn_sol_ingenua.pack(side=tk.LEFT, padx=5)
        
        # Boton solución voraz
        btn_sol_voraz = tk.Button(frame_botones_soluciones,  text="SOLUCIÓN VORAZ", fg='#ffe1f5', bg='#F1A7F1',
                                  font=custom_font_button, image=icono_sol_voraz, compound='top', width=140, height=100 ,command=lambda: procesar_ofertas(A, B, n, 3))
        btn_sol_voraz.pack(side=tk.LEFT, padx=5)

         # Boton solución dinamica
        btn_sol_dinamica = tk.Button(frame_botones_soluciones, text="SOLUCIÓN DINÁMICA", fg='#ffe1f5', bg='#F1A7F1',
                                     font=custom_font_button, image=icono_sol_dinamica, compound='top', width=140, height=100 ,command=lambda: procesar_ofertas(A, B, n, 2))
        btn_sol_dinamica.pack(side=tk.LEFT, padx=5)

        


        label_res = tk.Label(subcontenedor, text="Resultado", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_texto).pack(pady=(10, 0))
# ──── ✧《FRAME RESULTADOS》✧ ──── #
        contenedor_mostrar = tk.Frame(subcontenedor, bg='#e1faf6', width=400, height=400)
        contenedor_mostrar.pack_propagate(False)
        contenedor_mostrar.pack(pady=(10, 0))

        # Botón ATRÁS
        btn_atras = tk.Button(subcontenedor, text="ATRÁS ",  bg='#6fa1e4', fg='#ffffff', font=custom_font_button, image=atras, compound='right', width=300, height=50)
        btn_atras.pack(pady=(10, 0)) 
        
        
        
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
                 vm, ma = fuerza_bruta_sub(A, B,n+1, ofertas)
                 
                 
                 labelvm = tk.Label(contenedor_mostrar, text=f"Valor máximo: {vm}")
                 labelvm.pack(pady=5)
                 labelma = tk.Label(contenedor_mostrar, text=f"Mejor asignación")
                 labelma.pack(pady=5) 
                
                 for i in range(len(ma)):
                     if i == (len(ma) -1):
                            labelma = tk.Label(contenedor_mostrar, text=f"Oferta del gobierno: {ma[i]}")
                            labelma.pack(pady=5)
                     else:
                         labelma = tk.Label(contenedor_mostrar, text=f"Ofertador {i+1}: {ma[i]}")
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
                         labelma = tk.Label(contenedor_mostrar, text=f"Ofertador {i+1}: {vadin[i]}")
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
                         labelma = tk.Label(contenedor_mostrar, text=f"Ofertador {i+1}: {mavoraz[i]}")
                         labelma.pack(pady=5)              
                 end_time = time.time()
                 labeltime = tk.Label(contenedor_mostrar, text=f"Tiempo de ejecución: {end_time - start_time} segundos")
                 labeltime.pack(pady=5)
            except ValueError:
             messagebox.showerror("Error", "Por favor, ingresa ofertas válidas en el formato correcto.")
        def limpiar_contenedor():
            for widget in contenedor_mostrar.winfo_children():
                widget.destroy()
    
       
    
    #──── ✧《VENTANA PRINCIPAL》✧ ────#
    root = tk.Tk()
    root.title("SUBASTA")
    root.geometry("600x650")
    root.configure(bg='#6fa1e4')
    #──── ✧《✩》✧ ────#

    #──── ✧《CONTENEDORES》✧ ────#
    contenedor = tk.Frame(root, bg='#8FD4F7', width=535, height=535, bd=5, relief='ridge')
    contenedor.place(x=30, y=70)
    contenedor.pack_propagate(False)
    #──── ✧《✩》✧ ────#

    #──── ✧《FUENTE E ICONOS》✧ ────#
   

    custom_font_title = font.Font(family="Times New Roman", size=30, weight="bold")
    custom_font_texto = font.Font(family="Times New Roman", size=20, weight="bold")
    custom_font_button = font.Font(family="Times New Romans", size=10, weight="bold")

    inteligente = PhotoImage(file=os.path.join(iconos_dir, 'avanzar.png'))
    subasta = PhotoImage(file=os.path.join(iconos_dir, 'subasta.png'))
    atras = PhotoImage(file=os.path.join(iconos_dir, 'atras.png'))
    
    
    icono_sol_ingenua = PhotoImage(file=os.path.join(iconos_dir, 'ingenua.png'))  # Icono de solución ingenua
    icono_sol_voraz = PhotoImage(file=os.path.join(iconos_dir, 'voraz.png'))      # Icono de solución voraz
    icono_sol_dinamica = PhotoImage(file=os.path.join(iconos_dir, 'dinamica.png'))
    #──── ✧《✩》✧ ────#

    #──── ✧《TITULO》✧ ────#
    tk.Label(root, text="SUBASTA", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_title).pack(pady=(10, 0))
    #──── ✧《✩》✧ ────#

    #CONTENIDO DEL CONTENEDOR MENU

    label_A = tk.Label(contenedor, text="Ingrese total de acciones:", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_texto).pack(pady=(10, 0))
    entry_A = tk.Entry(contenedor)
    entry_A.pack(pady=(0, 10))
    entry_A = tk.Entry(entry_A, width=23, font=('Arial', 14))
    entry_A.pack(side=tk.LEFT)

    label_B = tk.Label(contenedor, text="Ingrese precio minimo de acción:", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_texto).pack(pady=(10, 0))
    entry_B = tk.Entry(contenedor)
    entry_B.pack(pady=(0, 10))
    entry_B = tk.Entry(entry_B, width=23, font=('Arial', 14))
    entry_B.pack(side=tk.LEFT)

    label_n = tk.Label(contenedor, text="Ingrese numero de oferentes:", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_texto).pack(pady=(10, 0))
    entry_n = tk.Entry(contenedor)
    entry_n.pack(pady=(0, 10))
    entry_n = tk.Entry(entry_n, width=23, font=('Arial', 14))
    entry_n.pack(side=tk.LEFT)

    # Botón para obtener los valores
    # BOTON TERMINAL INTELIGENTE
    button_submit = tk.Button(contenedor, text=" INGRESAR ", bg='#6fa1e4', fg='#ffffff', font=custom_font_button, image=inteligente, compound='right',command=obtener_valores, width=300, height=50)
    button_submit.pack(pady=(10, 10)) 
    # BOTON ATRÁS
    btn_atras = tk.Button(contenedor, text="ATRÁS ", fg = '#ffe1f5', bg='#F1A7F1', font=custom_font_button, image=atras, compound='right', width=300, height=50)
    btn_atras.pack(pady=(10, 0))
    root.mainloop()


