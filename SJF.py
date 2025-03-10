import matplotlib.pyplot as plt 
import tkinter as tk 
from tkinter import simpledialog 
from matplotlib.widgets import Button  


def tabla_SJF():
    root = tk.Tk()  
    root.withdraw() 

    # Solicitamos al usuario la cantidad de procesos a ingresar
    cantidad_procesos = simpledialog.askinteger("Entrada", "Ingrese la cantidad de procesos:")

    # Definimos las columnas de la tabla
    columnas = ["Proceso", "Ráfaga", "Tiempo", "Prioridad"]
    filas = []  # Lista para almacenar los datos de cada proceso

    # Bucle para solicitar los datos de cada proceso
    for i in range(cantidad_procesos):
        rafaga = simpledialog.askinteger("Entrada", f"Ráfaga del Proceso {i + 1}:")  
        tiempo = simpledialog.askinteger("Entrada", f"Tiempo del Proceso {i + 1}:") 
        prioridad = simpledialog.askinteger("Entrada", f"Prioridad del Proceso {i + 1}:")  
        filas.append([i + 1, rafaga, tiempo, prioridad])  # Guardamos los datos en la lista

   
    fig, ax = plt.subplots(figsize=(6, 3))  
    ax.axis('tight') 
    ax.axis('off') 
    ax.table(cellText=filas, colLabels=columnas, cellLoc='center', loc='center')  

  
    def on_click(event):
        plt.close(fig)  
        import subprocess 
        subprocess.run(["python", "gantt.py"]) 

   
    ax_button = plt.axes([0.4, 0.02, 0.2, 0.075])  
    button = Button(ax_button, 'Ver Gantt')  
    button.on_clicked(on_click)  
    plt.show() 
    
    return filas  
