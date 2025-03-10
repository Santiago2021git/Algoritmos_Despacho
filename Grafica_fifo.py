import matplotlib.pyplot as plt
import numpy as np  
from Fifo import tabla_fifo  
from matplotlib.widgets import Button 
from Te_fifo import mostrar_tabla_tiempos_espera
from Ts_fifo import mostrar_tabla_tiempos_sistema

def generar_fifo():
    # Obtener los datos desde tabla_fifo() en Fifo.py
    procesos = tabla_fifo()

    if not procesos:
        print("No hay procesos para mostrar.")
        return

    # Listas para almacenar los datos procesados
    tareas = []
    total_tiempo = 0  # El primer proceso inicia en 0

    # Procesar los datos obtenidos
    for i, proceso in enumerate(procesos):
        pid, rafaga, tiempo, prioridad = proceso  # Extraer datos

        if i == 0:
            # El primer proceso inicia en 0, ignorando su tiempo de llegada
            inicio = 0
        else:
            # El siguiente proceso empieza donde terminó el anterior o cuando llega, lo que sea mayor
            inicio = max(total_tiempo, tiempo)

        fin = inicio + rafaga
        tareas.append((f"Proceso {pid}", inicio, fin))

        # Actualizar el tiempo total acumulado
        total_tiempo = fin

   
    fig, ax = plt.subplots(figsize=(10, 5))

    for tarea, inicio, fin in tareas:
        ax.barh(tarea, fin - inicio, left=inicio, color="mediumpurple", edgecolor="black")

   
    ax.set_xticks(np.arange(0, total_tiempo + 1, 1))
    ax.set_xlim(0, total_tiempo)  

    
    plt.xlabel("Tiempo") 
    plt.ylabel("Procesos")  
    plt.title("Planificación FIFO")  
    plt.grid(axis="x", linestyle="--", alpha=0.7) 

    ax_button = plt.axes([0.4, 0.02, 0.2, 0.075]) 
    button = Button(ax_button, 'Cálculo de Tiempos')

    def on_click(event):
        mostrar_tabla_tiempos_espera(procesos)
        mostrar_tabla_tiempos_sistema(procesos)

    button.on_clicked(on_click)

    plt.show()


#generar_fifo()

# colores = ["skyblue", "lightcoral", "lightgreen", "gold", "mediumpurple"]


