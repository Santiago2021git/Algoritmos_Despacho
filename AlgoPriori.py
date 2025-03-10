import matplotlib.pyplot as plt  
import tkinter as tk  
from tkinter import simpledialog 
from matplotlib.widgets import Button 


def tabla_AlgoPriori():
    root = tk.Tk()  
    root.withdraw()  

    cantidad_procesos = simpledialog.askinteger("Entrada", "Ingrese la cantidad de procesos:")

 
    columnas = ["Proceso", "Ráfaga", "Tiempo", "Prioridad"]
    filas = []  # Lista para almacenar los datos de cada proceso

   
    for i in range(cantidad_procesos):
        rafaga = simpledialog.askinteger("Entrada", f"Ráfaga del Proceso {i + 1}:") 
        tiempo = simpledialog.askinteger("Entrada", f"Tiempo del Proceso {i + 1}:")  
        prioridad = simpledialog.askinteger("Entrada", f"Prioridad del Proceso {i + 1}:")  
        filas.append([i + 1, rafaga, tiempo, prioridad])  

   
    fig, ax = plt.subplots(figsize=(6, 3))  # Define el tamaño de la tabla
    ax.axis('tight')  # Ajusta la tabla al espacio disponible
    ax.axis('off')  # Oculta los ejes para que solo se vea la tabla
    ax.table(cellText=filas, colLabels=columnas, cellLoc='center', loc='center')  # Crea la tabla con los datos

  
    def on_click(event):
        plt.close(fig)  # Cierra la ventana de la tabla
        import subprocess  # Importamos subprocess para ejecutar otro script
        subprocess.run(["python", "gantt.py"])  # Ejecuta el script gantt.py en una nueva ventana

    
    ax_button = plt.axes([0.4, 0.02, 0.2, 0.075])  # Definimos la posición y tamaño del botón
    button = Button(ax_button, 'Ver Gantt')  # Creamos el botón con la etiqueta "Ver Gantt"
    button.on_clicked(on_click)  # Asociamos la función on_click al botón

    plt.show()  # Muestra la tabla con el botón

    return filas  # Devolvemos los datos ingresados por el usuario


