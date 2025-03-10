import matplotlib.pyplot as plt  # Importar la librería para gráficos
import numpy as np  # Manejo de arrays numéricos
from AlgoPriori import tabla_AlgoPriori  # Obtener los datos
from matplotlib.widgets import Button
from Te_AlgoPriori import mostrar_tabla_tiempos_espera
from Ts_AlgoPriori import mostrar_tabla_tiempos_sistema

def generar_AlgoritmoPrioridad():
    # Obtener los datos desde tabla_AlgoPriori() en AlgoPriori.py
    procesos = tabla_AlgoPriori()

    if not procesos:
        print("No hay procesos para mostrar.")
        return
    
    # Ordenar procesos por prioridad (menor número = mayor prioridad)
    procesos.sort(key=lambda x: x[3])  # Ordenar solo por prioridad

    tareas = []
    tiempo_actual = 0  # Tiempo acumulado en la ejecución

    for i, proceso in enumerate(procesos):
        pid, rafaga, tiempo_llegada, prioridad = proceso  # Extraer datos
        
        # Si es el primer proceso, debe comenzar en 0
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
        ax.barh(tarea, fin - inicio, left=inicio, color="royalblue", edgecolor="black")

    ax.set_xticks(np.arange(0, tiempo_actual + 1, 1))  # Ajustar el eje X
    ax.set_xlim(0, tiempo_actual)  # Límite del eje X

    # Etiquetas y título del gráfico
    plt.xlabel("Tiempo")
    plt.ylabel("Procesos")
    plt.title("Algoritmo de prioridad")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    
    # Botón para mostrar tablas de tiempos
    ax_button = plt.axes([0.4, 0.02, 0.2, 0.075])
    button = Button(ax_button, 'Cálculo de Tiempos')

    def on_click(event):
        mostrar_tabla_tiempos_espera(procesos)
        mostrar_tabla_tiempos_sistema(procesos)
    
    button.on_clicked(on_click)
    
    plt.show()