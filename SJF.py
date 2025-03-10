import matplotlib.pyplot as plt  # Para generar gráficos y tablas
import tkinter as tk  # Para crear cuadros de diálogo e interfaces gráficas
from tkinter import simpledialog  # Para capturar datos de entrada del usuario
from matplotlib.widgets import Button  # Para agregar botones a la interfaz de Matplotlib

# Definimos la función tabla_fifo, que solicita datos y muestra una tabla
def tabla_SJF():
    root = tk.Tk()  # Creamos una ventana de Tkinter
    root.withdraw()  # Ocultamos la ventana principal, solo usaremos los cuadros de diálogo

    # Solicitamos al usuario la cantidad de procesos a ingresar
    cantidad_procesos = simpledialog.askinteger("Entrada", "Ingrese la cantidad de procesos:")

    # Definimos las columnas de la tabla
    columnas = ["Proceso", "Ráfaga", "Tiempo", "Prioridad"]
    filas = []  # Lista para almacenar los datos de cada proceso

    # Bucle para solicitar los datos de cada proceso
    for i in range(cantidad_procesos):
        rafaga = simpledialog.askinteger("Entrada", f"Ráfaga del Proceso {i + 1}:")  # Duración del proceso
        tiempo = simpledialog.askinteger("Entrada", f"Tiempo del Proceso {i + 1}:")  # Cuándo inicia el proceso
        prioridad = simpledialog.askinteger("Entrada", f"Prioridad del Proceso {i + 1}:")  # Prioridad del proceso
        filas.append([i + 1, rafaga, tiempo, prioridad])  # Guardamos los datos en la lista

    # Crear una figura y un eje para mostrar la tabla
    fig, ax = plt.subplots(figsize=(6, 3))  # Define el tamaño de la tabla
    ax.axis('tight')  # Ajusta la tabla al espacio disponible
    ax.axis('off')  # Oculta los ejes para que solo se vea la tabla
    ax.table(cellText=filas, colLabels=columnas, cellLoc='center', loc='center')  # Crea la tabla con los datos

    # Definimos una función para abrir el script gantt.py cuando se presiona un botón
    def on_click(event):
        plt.close(fig)  # Cierra la ventana de la tabla
        import subprocess  # Importamos subprocess para ejecutar otro script
        subprocess.run(["python", "gantt.py"])  # Ejecuta el script gantt.py en una nueva ventana

    # Crear un botón en la interfaz
    ax_button = plt.axes([0.4, 0.02, 0.2, 0.075])  # Definimos la posición y tamaño del botón
    button = Button(ax_button, 'Ver Gantt')  # Creamos el botón con la etiqueta "Ver Gantt"
    button.on_clicked(on_click)  # Asociamos la función on_click al botón

    plt.show()  # Muestra la tabla con el botón

    return filas  # Devolvemos los datos ingresados por el usuario
