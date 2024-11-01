
import tkinter as tk
from tkinter import PhotoImage, font  
import os
from . import ventana_terminal_inteligente
from . import subasta
iconos_dir = os.path.join(os.path.dirname(__file__), 'ICONOS')

#funciones
def ventana_principal():
    #──── ✧《VENTANA PRINCIPAL》✧ ────#
    root = tk.Tk()
    root.title("Pagina Principal")
    root.geometry("970x650")
    root.configure(bg='#6fa1e4')
    #──── ✧《✩》✧ ────#

    #──── ✧《CONTENEDORES》✧ ────#
    contenedor_menu = tk.Frame(root, bg='#8FD4F7', width=535, height=535)
    contenedor_menu.place(x=200, y=70)
    contenedor_menu.pack_propagate(False)
    #──── ✧《✩》✧ ────#

    #──── ✧《FUENTE E ICONOS》✧ ────#
    custom_font_title = font.Font(family="Times New Roman", size=30, weight="bold")

    avanzar = PhotoImage(file=os.path.join(iconos_dir, 'kitty.png'))
    #──── ✧《✩》✧ ────#

    #──── ✧《TITULO》✧ ────#
    tk.Label(root, text="MENÚ PRINCIPAL", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_title).pack(pady=(10, 0))
    #──── ✧《✩》✧ ────#
    def ventana_t():
        #destruir esta ventana y ejecutar la siguiente
        root.destroy()
        ventana_terminal_inteligente.ventana_terminal()
        
    def ventana_s():
        #destruir esta ventana y ejecutar la siguiente
        root.destroy()
        subasta.subastaVentana()
    #CONTENIDO DEL CONTENEDOR MENU
    tk.Label(contenedor_menu, text="Selecciona una opción:", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_title).pack(pady=(10, 0))
    tk.Button(contenedor_menu, text="Terminal inteligente😼", bg='#6fa1e4', bd=0, font=('Helvetica', 16),  width=20, height=3, command=ventana_t).pack(pady=(10, 0))
    tk.Button(contenedor_menu, text="Subasta 🐈‍",  bg='#6fa1e4', bd=0, font=('Helvetica', 16),  width=20, height=3,command=ventana_s).pack(pady=(10, 0))
    root.mainloop()
    