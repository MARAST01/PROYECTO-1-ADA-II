import tkinter as tk
from tkinter import PhotoImage, font  
import os
iconos_dir = os.path.join(os.path.dirname(__file__), 'ICONOS')

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

#CONTENIDO DEL CONTENEDOR MENU
tk.Label(contenedor_menu, text="Selecciona una opción:", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_title).pack(pady=(10, 0))
tk.Button(contenedor_menu, text="Terminal inteligente", image=avanzar, bg='#6fa1e4', bd=0).pack(pady=(10, 0))
tk.Button(contenedor_menu, text="Subasta", image=avanzar, bg='#6fa1e4', bd=0).pack(pady=(10, 0))

root.mainloop()