import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabla con Treeview")

# Crear el Treeview
tree = ttk.Treeview(root, columns=(1,2,3,4,5,6,7,8), show="headings")

# Encabezados de columna
tree.heading(1, text="Columna 1")
tree.heading(2, text="Columna 2")
tree.heading(3, text="Columna 3")
tree.heading(4, text="Columna 4")
tree.heading(5, text="Columna 5")
tree.heading(6, text="Columna 6")
tree.heading(7, text="Columna 7")
tree.heading(8, text="Columna 8")

# Anchura de columna
tree.column(1, width=100)
tree.column(2, width=100)
tree.column(3, width=100)
tree.column(4, width=100)
tree.column(5, width=100)
tree.column(6, width=100)
tree.column(7, width=100)
tree.column(8, width=100)

# Insertar datos en la tabla
tree.insert("", "end", values=("Fila 1", "Fila 1", "Fila 1", "Fila 1", "Fila 1", "Fila 1", "Fila 1", "Fila 1"))
tree.insert("", "end", values=("Fila 2", "Fila 2", "Fila 2", "Fila 2", "Fila 2", "Fila 2", "Fila 2", "Fila 2"))
tree.insert("", "end", values=("Fila 3", "Fila 3", "Fila 3", "Fila 3", "Fila 3", "Fila 3", "Fila 3", "Fila 3"))

# Ajustar el Treeview en la ventana
tree.pack(side="left", fill="y")

# Crear una barra de desplazamiento vertical
scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar_y.pack(side="right", fill="y")

# Configurar la barra de desplazamiento vertical para el Treeview
tree.configure(yscrollcommand=scrollbar_y.set)

# Crear una barra de desplazamiento horizontal
scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
scrollbar_x.pack(side="bottom", fill="x")

# Configurar la barra de desplazamiento horizontal para el Treeview
tree.configure(xscrollcommand=scrollbar_x.set)

root.mainloop()
