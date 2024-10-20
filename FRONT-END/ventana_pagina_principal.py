#ya me harté de que no me deje hacer push (esto lo escribió copilot pero concuerdo con él)
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
contenedor_menu = tk.Frame(root, bg='#8FD4F7', width=535, height=535, bd=5, relief='ridge')
contenedor_menu.place(x=200, y=70)
contenedor_menu.pack_propagate(False)
#──── ✧《✩》✧ ────#

#──── ✧《FUENTE E ICONOS》✧ ────#
custom_font_title = font.Font(family="Times New Roman", size=30, weight="bold")
custom_font_button = font.Font(family="Times New Romans", size=10, weight="bold")

inteligente = PhotoImage(file=os.path.join(iconos_dir, 'inteligente.png'))
subasta = PhotoImage(file=os.path.join(iconos_dir, 'subasta.png'))
salir = PhotoImage(file=os.path.join(iconos_dir, 'salir.png'))
#──── ✧《✩》✧ ────#

#──── ✧《TITULO》✧ ────#
tk.Label(root, text="MENÚ PRINCIPAL", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_title).pack(pady=(10, 0))
#──── ✧《✩》✧ ────#

#CONTENIDO DEL CONTENEDOR MENU
tk.Label(contenedor_menu, text="Selecciona una opción:", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_title).pack(pady=(10, 0))
# BOTON TERMINAL INTELIGENTE
btn_term = tk.Button(contenedor_menu, text=" TERMINAL INTELIGENTE ", fg = '#ffe1f5', bg='#F1A7F1', font=custom_font_button, image=inteligente, compound='right', width=300, height=50)
btn_term.pack(pady=(10, 10)) 
# BOTON SUBASTA
btn_sub = tk.Button(contenedor_menu, text=" SUBASTA ", fg = '#ffe1f5', bg='#F1A7F1', font=custom_font_button, image=subasta, compound='right', width=300, height=50)
btn_sub.pack(pady=(10, 10)) 
# BOTON SALIR
btn_sub = tk.Button(contenedor_menu, text=" SALIR ", fg = '#ffe1f5', bg='#F1A7F1', font=custom_font_button, image=salir, compound='right', width=300, height=50)
btn_sub.pack(pady=(10, 10)) 

root.mainloop()