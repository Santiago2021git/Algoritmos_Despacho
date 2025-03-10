import tkinter as tk  # Importar la librería para la interfaz gráfica
from tkinter import PhotoImage  # Permite cargar imágenes
from Grafica_fifo import generar_fifo
from Grafica_AlgoPriori import generar_AlgoritmoPrioridad
from Grafica_SJF import generar_SJF

# Función para ocultar la ventana principal al presionar un botón
def ocultar_ventana():
    root.withdraw()  # Oculta la ventana principal

# Función para salir de la aplicación
def salir():
    root.destroy()  # Cierra la ventana principal

# Crear la ventana principal
root = tk.Tk()
root.title("Algoritmos de Planificación")
root.geometry("600x300")  # Aumentar el tamaño de la ventana
root.resizable(False, False)  # Evitar que se redimensione

# Cargar imagen de fondo (debe estar en la misma carpeta que el script)
try:
    fondo = PhotoImage(file="imagen.png")  # Reemplaza con tu imagen
    background_label = tk.Label(root, image=fondo)
    background_label.place(relwidth=1, relheight=1)  # Ajustar la imagen al tamaño de la ventana
except:
    root.configure(bg="#D3E0EA")  # Color de fondo si no se encuentra la imagen

# Crear un marco para organizar los botones
frame = tk.Frame(root, bg="#A2B5BB", bd=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear los botones con estilos mejorados
btn_prioridad = tk.Button(frame, text="Algoritmo Prioridad", 
                          command=lambda: [ocultar_ventana(), generar_AlgoritmoPrioridad()],
                          font=("Arial", 12), bg="#4CAF50", fg="white", width=20)

btn_fifo = tk.Button(frame, text="FIFO", 
                     command=lambda: [ocultar_ventana(), generar_fifo()],
                     font=("Arial", 12), bg="#2196F3", fg="white", width=20)

btn_sjf = tk.Button(frame, text="SJF", 
                    command=lambda: [ocultar_ventana(), generar_SJF()],
                    font=("Arial", 12), bg="#FF9800", fg="white", width=20)

btn_salir = tk.Button(frame, text="Salir", command=salir, 
                      font=("Arial", 12), bg="#F44336", fg="white", width=20)

# Ubicar los botones en el marco
btn_prioridad.pack(pady=5)
btn_fifo.pack(pady=5)
btn_sjf.pack(pady=5)
btn_salir.pack(pady=5)

# Ejecutar la ventana
root.mainloop()


