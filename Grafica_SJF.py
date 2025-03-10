import matplotlib.pyplot as plt  # Importar la librería para gráficos 
import numpy as np  # Manejo de arrays numéricos
from SJF import tabla_SJF  # Obtener los datos
from matplotlib.widgets import Button
from Te_SJF import mostrar_tabla_tiempos_espera
from Ts_SJF import mostrar_tabla_tiempos_sistema

def generar_SJF():
    # Obtener los datos desde tabla_SJF() en SJF.py
    procesos = tabla_SJF()

    if not procesos:
        print("No hay procesos para mostrar.")
        return

    # Asegurar que el primer proceso sea el primero en la lista
    primer_proceso = procesos[0]
    procesos_restantes = procesos[1:]

    # Ordenar el resto de los procesos por ráfaga de CPU (menor a mayor)
    procesos_restantes.sort(key=lambda x: x[1])  

    # Unir el primer proceso con los ordenados
    procesos = [primer_proceso] + procesos_restantes  

    tareas = []
    tiempo_actual = 0  # Tiempo acumulado en la ejecución

    for i, proceso in enumerate(procesos):
        pid, rafaga, tiempo_llegada, prioridad = proceso  # Extraer datos
        
        # Asegurar que el primer proceso siempre inicie en 0
        if i == 0:
            inicio = 0
        else:
            inicio = max(tiempo_actual, tiempo_llegada)
        
        fin = inicio + rafaga
        tareas.append((f"Proceso {pid}", inicio, fin))
        
        # Actualizar el tiempo actual
        tiempo_actual = fin
    
    # Crear el diagrama de Gantt
    fig, ax = plt.subplots(figsize=(10, 5))

    for tarea, inicio, fin in tareas:
        ax.barh(tarea, fin - inicio, left=inicio, color="seagreen", edgecolor="black")

    ax.set_xticks(np.arange(0, tiempo_actual + 1, 1))  # Ajustar el eje X
    ax.set_xlim(0, tiempo_actual)  # Límite del eje X

    # Etiquetas y título del gráfico
    plt.xlabel("Tiempo")
    plt.ylabel("Procesos")
    plt.title("SJF")
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    # Botón para mostrar tablas de tiempos
    ax_button = plt.axes([0.4, 0.02, 0.2, 0.075])
    button = Button(ax_button, 'Cálculo de Tiempos')

    def on_click(event):
        mostrar_tabla_tiempos_espera(procesos)
        mostrar_tabla_tiempos_sistema(procesos)
    
    button.on_clicked(on_click)
    
    plt.show()
