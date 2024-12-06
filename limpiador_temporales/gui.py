import tkinter as tk
from tkinter import messagebox
from .cleaner import limpiar_archivos_temporales  # Importación relativa

def crear_interfaz():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Limpiador de Archivos Temporales")
    root.geometry("300x150")

    # Crear un botón para iniciar la limpieza
    boton_limpiar = tk.Button(root, text="Limpiar Archivos Temporales", command=lambda: (limpiar_archivos_temporales(), messagebox.showinfo("Limpieza Completa", "Todos los archivos temporales han sido eliminados.")))
    boton_limpiar.pack(pady=20)

    # Iniciar el bucle principal de la aplicación
    root.mainloop()
