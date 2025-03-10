import tkinter as tk  
from tkinter import PhotoImage  
from Grafica_fifo import generar_fifo
from Grafica_AlgoPriori import generar_AlgoritmoPrioridad
from Grafica_SJF import generar_SJF


def ocultar_ventana():
    root.withdraw()  


def salir():
    root.destroy()  


root = tk.Tk()
root.title("Algoritmos de Planificación")
root.geometry("600x300")  
root.resizable(False, False)  


try:
    fondo = PhotoImage(file="imagen.png")  
    background_label = tk.Label(root, image=fondo)
    background_label.place(relwidth=1, relheight=1)  
except:
    root.configure(bg="#D3E0EA")  


frame = tk.Frame(root, bg="#A2B5BB", bd=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


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


btn_prioridad.pack(pady=5)
btn_fifo.pack(pady=5)
btn_sjf.pack(pady=5)
btn_salir.pack(pady=5)


root.mainloop()


