import tkinter as tk
from tkinter import PhotoImage, font  
import os
iconos_dir = os.path.join(os.path.dirname(__file__), 'ICONOS')

#──── ✧《VENTANA PRINCIPAL》✧ ────#
root = tk.Tk()
root.title("Terminal Inteligente")
root.geometry("970x650")
root.configure(bg='#6fa1e4')
#──── ✧《✩》✧ ────#

#esta función la borro después. Es solo para que no marque error en la línea 107
def nombre_función_backend():
    pass

#──── ✧《CONTENEDORES》✧ ────#
# Contenedor: costos - AVANZAR, BORRAR, REEMPLAZAR, INSERTAR y MATAR
frame_costos = tk.Frame(root, bg='#8FD4F7', width=400, height=535)
frame_costos.place(x=10, y=70)
frame_costos.pack_propagate(False)

# Contenedor: datos - PALABRA INICIAL, PALABRA FINAL, COSTOS y TIEMPO
frame_datos = tk.Frame(root, bg='#6fa1e4')
frame_datos.place(x=420, y=70, width=500, height=600)
#──── ✧《✩》✧ ────#

#──── ✧《FUENTE E ICONOS》✧ ────#
# Fuente personalizada
custom_font_label = font.Font(family="Times New Roman", size=18)
custom_font_button = font.Font(family="Helvetica", size=10, weight="bold")
custom_font_title = font.Font(family="Times New Roman", size=30, weight="bold")

# íconos contenedor costos
avanzar = PhotoImage(file=os.path.join(iconos_dir, 'avanzar.png'))
borrar = PhotoImage(file=os.path.join(iconos_dir, 'borrar.png'))
reemplazar = PhotoImage(file=os.path.join(iconos_dir, 'reemplazar.png')) 
insertar = PhotoImage(file=os.path.join(iconos_dir, 'insertar.png')) 
kill = PhotoImage(file=os.path.join(iconos_dir, 'dead.png')) 

# íconos contenedor frame_boton_soluciones
icono_sol_ingenua = PhotoImage(file=os.path.join(iconos_dir, 'ingenua.png')) 
icono_sol_voraz = PhotoImage(file=os.path.join(iconos_dir, 'voraz.png')) 
icono_sol_dinamica = PhotoImage(file=os.path.join(iconos_dir, 'dinamica.png')) 

# íconos contenedor frame_datos
icono_atras = PhotoImage(file=os.path.join(iconos_dir, 'atras.png'))
icono_grafica = PhotoImage(file=os.path.join(iconos_dir, 'grafica.png'))
icono_tiempo = PhotoImage(file=os.path.join(iconos_dir, 'tiempo.png'))
icono_ver = PhotoImage(file=os.path.join(iconos_dir, 'ver.png'))
#──── ✧《✩》✧ ────#

#──── ✧《TITULO》✧ ────#
tk.Label(root, text="TERMINAL INTELIGENTE", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_title).pack(pady=(10, 0))
#──── ✧《✩》✧ ────#

#──── ✧《CONTENIDO DEL CONTENEDOR COSTOS》✧ ────#
# Crear manualmente cada etiqueta, entrada y su ícono

# Avanzar
tk.Label(frame_costos, text="avanzar", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_label).pack(pady=(10, 0))
frame_entry1 = tk.Frame(frame_costos)
frame_entry1.pack(pady=(0, 10))

entry1 = tk.Entry(frame_entry1, width=23, font=('Arial', 14))
entry1.pack(side=tk.LEFT)

icon_label1 = tk.Label(frame_entry1, image=avanzar, bg='#8FD4F7')
icon_label1.pack(side=tk.LEFT)

# Borrar
tk.Label(frame_costos, text="borrar", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_label).pack(pady=(10, 0))
frame_entry2 = tk.Frame(frame_costos)
frame_entry2.pack(pady=(0, 10))

entry2 = tk.Entry(frame_entry2, width=23, font=('Arial', 14))
entry2.pack(side=tk.LEFT)

icon_label2 = tk.Label(frame_entry2, image=borrar, bg='#8FD4F7')
icon_label2.pack(side=tk.LEFT)

# Reemplazar
tk.Label(frame_costos, text="reemplazar", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_label).pack(pady=(10, 0))
frame_entry3 = tk.Frame(frame_costos)
frame_entry3.pack(pady=(0, 10))

entry3 = tk.Entry(frame_entry3, width=23, font=('Arial', 14))
entry3.pack(side=tk.LEFT)

icon_label3 = tk.Label(frame_entry3, image=reemplazar, bg='#8FD4F7')
icon_label3.pack(side=tk.LEFT)

# Insertar
tk.Label(frame_costos, text="insertar", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_label).pack(pady=(10, 0))
frame_entry4 = tk.Frame(frame_costos)
frame_entry4.pack(pady=(0, 10))

entry4 = tk.Entry(frame_entry4, width=23, font=('Arial', 14))
entry4.pack(side=tk.LEFT)

icon_label4 = tk.Label(frame_entry4, image=insertar, bg='#8FD4F7')
icon_label4.pack(side=tk.LEFT)

# Matar
tk.Label(frame_costos, text="matar", fg='#6fa1e4', bg='#8FD4F7', font=custom_font_label).pack(pady=(10, 0))
frame_entry5 = tk.Frame(frame_costos)
frame_entry5.pack(pady=(0, 10))

entry5 = tk.Entry(frame_entry5, width=23, font=('Arial', 14))
entry5.pack(side=tk.LEFT)

icon_label5 = tk.Label(frame_entry5, image=kill, bg='#8FD4F7')
icon_label5.pack(side=tk.LEFT)

# Botón para guardar costos
btn_guardar_costos = tk.Button(frame_costos, text="GUARDAR COSTOS", bg='#6fa1e4', fg='#8FD4F7', font=custom_font_button, width=35, height=2)
btn_guardar_costos.pack(pady=20)
#──── ✧《✩》✧ ────#

#──── ✧《CONTENIDO DEL CONTENEDOR DATOS》✧ ────#
#palabra inicial/final, botones de solución, costos, tiempo, boton de gráfica y atrás.
# palabra inicial
tk.Label(frame_datos, text="PALABRA INICIAL", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_label).pack(pady=(10, 0))
palabra_inicial = tk.Entry(frame_datos, width=25, font=('Arial', 14))
palabra_inicial.pack(pady=(0, 10), ipady=10)

# palabra final
tk.Label(frame_datos, text="PALABRA FINAL", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_label).pack(pady=(10, 0))
palabra_final = tk.Entry(frame_datos, width=25, font=('Arial', 14))
palabra_final.pack(pady=(0, 10), ipady=10)

#──── ✧《BOTONES DE SOLUCIÓN》✧ ────#
# Contenedor: botones de soluciones y colocarlos en fila
frame_botones_soluciones = tk.Frame(frame_datos, bg='#6fa1e4')
frame_botones_soluciones.pack(pady=(10, 0))

# Boton solución ingenua
btn_sol_ingenua = tk.Button(frame_botones_soluciones, text="SOLUCIÓN INGENUA", fg='#ffe1f5', bg='#F1A7F1',
                            font=custom_font_button, image=icono_sol_ingenua, compound='top', width=140, height=100)
btn_sol_ingenua.pack(side=tk.LEFT, padx=5)

# Boton solución voraz
btn_sol_voraz = tk.Button(frame_botones_soluciones, text="SOLUCIÓN VORAZ", fg='#ffe1f5', bg='#F1A7F1',
                          font=custom_font_button, image=icono_sol_voraz, compound='top', width=140, height=100)
btn_sol_voraz.pack(side=tk.LEFT, padx=5)

# Boton solución dinamica
btn_sol_dinamica = tk.Button(frame_botones_soluciones, text="SOLUCIÓN DINÁMICA", fg='#ffe1f5', bg='#F1A7F1',
                             font=custom_font_button, image=icono_sol_dinamica, compound='top', width=140, height=100)
btn_sol_dinamica.pack(side=tk.LEFT, padx=5)
#──── ✧《✩》✧ ────#

#──── ✧《TIEMPO Y COSTOS》✧ ────#
# Contenedor: costos_tiempo - COSTOS y TIEMPO
frame_costos_tiempo = tk.Frame(frame_datos, bg='#6fa1e4')
frame_costos_tiempo.pack(pady=(10, 0))
# Crear un frame individual para la columna de "COSTOS"
frame_costos = tk.Frame(frame_costos_tiempo, bg='#6fa1e4')
frame_costos.pack(side=tk.LEFT, padx=20)
#contenedor: alinear botones en fila
frame_botones_ver = tk.Frame(frame_datos, bg='#6fa1e4')
frame_botones_ver.pack(pady=(10, 0))

# Etiqueta y entrada para costos
tk.Label(frame_costos, text="COSTOS", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_label).pack(side=tk.TOP, pady=(0, 5))
costos = tk.Text(frame_costos, height=2, width=12)
costos.pack(side=tk.TOP, pady=(0, 10), ipady=10)

# Botón mostrar costos
btn_mostrar_costos = tk.Button(frame_botones_ver, command=nombre_función_backend, text="VER COSTOS ", fg = '#6fa1e4' , bg='#8FD4F7', font=custom_font_button, image=icono_ver, compound='right', width=130, height=50)
btn_mostrar_costos.pack(side=tk.LEFT, padx=5)

# Crear un frame individual para la columna de "TIEMPO"
frame_tiempo = tk.Frame(frame_costos_tiempo, bg='#6fa1e4')
frame_tiempo.pack(side=tk.LEFT, padx=20)

# Etiqueta y entrada para tiempo
tk.Label(frame_tiempo, text="TIEMPO", fg='#8FD4F7', bg='#6fa1e4', font=custom_font_label).pack(side=tk.TOP, pady=(0, 5))
tiempo = tk.Text(frame_tiempo, height=2, width=12)
tiempo.pack(side=tk.TOP, pady=(0, 10), ipady=10)

# Botón mostrar tiempo
btn_mostrar_tiempo = tk.Button(frame_botones_ver, command=nombre_función_backend, text="VER TIEMPO ", fg = '#6fa1e4' , bg='#8FD4F7', font=custom_font_button, image=icono_tiempo, compound='right', width=130, height=50)
btn_mostrar_tiempo.pack(side=tk.LEFT, padx=5)
#──── ✧《✩》✧ ────#

#──── ✧《BOTÓN GRAFICA Y ATRÁS》✧ ────#
# Botón de mostrar gráfica
btn_mostrar_grafica = tk.Button(frame_botones_ver, text="VER GRÁFICA ", fg = '#6fa1e4' , bg='#8FD4F7', font=custom_font_button, image=icono_grafica, compound='right', width=130, height=50)
btn_mostrar_grafica.pack(side=tk.LEFT, padx=5)

# Botón atrás
btn_atras = tk.Button(frame_datos, text="ATRÁS ", fg = '#ffe1f5', bg='#F1A7F1', font=custom_font_button, image=icono_atras, compound='right', width=1000, height=50)
btn_atras.pack(pady=(10, 0))  # Lo colocamos en el frame_datos
#──── ✧《✩》✧ ────#

#──── ✧《✩》✧ ────#

