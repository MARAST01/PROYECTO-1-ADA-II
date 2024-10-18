#EN PROCESO NO TOCAR 

import tkinter as tk
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
button_submit = tk.Button(root, text="Ingresar")
button_submit.pack(pady=20)
# Iniciar el bucle principal de la interfaz

root.mainloop()
