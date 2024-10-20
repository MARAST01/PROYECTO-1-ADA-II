import tkinter as tk
from tkinter import PhotoImage, font  
import os

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
iconos_dir = os.path.join(os.path.dirname(__file__), 'ICONOS')

custom_font_title = font.Font(family="Times New Roman", size=30, weight="bold")
custom_font_texto = font.Font(family="Times New Roman", size=20, weight="bold")
custom_font_button = font.Font(family="Times New Romans", size=10, weight="bold")

inteligente = PhotoImage(file=os.path.join(iconos_dir, 'avanzar.png'))
subasta = PhotoImage(file=os.path.join(iconos_dir, 'subasta.png'))
atras = PhotoImage(file=os.path.join(iconos_dir, 'atras.png'))
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
button_submit = tk.Button(contenedor, text=" INGRESAR ", bg='#6fa1e4', fg='#ffffff', font=custom_font_button, image=inteligente, compound='right', width=300, height=50)
button_submit.pack(pady=(10, 10)) 
# BOTON ATRÁS
btn_atras = tk.Button(contenedor, text="ATRÁS ", fg = '#ffe1f5', bg='#F1A7F1', font=custom_font_button, image=atras, compound='right', width=300, height=50)
btn_atras.pack(pady=(10, 0))
# Iniciar el bucle principal de la interfaz
root.mainloop()
