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
    
    # Separar el proceso 1 y los demás
    proceso_1 = next((p for p in procesos if p[0] == 1), None)
    otros_procesos = [p for p in procesos if p[0] != 1]
    
    # Ordenar los demás procesos por prioridad (menor número = mayor prioridad)
    otros_procesos.sort(key=lambda x: x[3])
    
    # Reconstruir la lista de procesos asegurando que "1" vaya primero
    procesos_ordenados = [proceso_1] + otros_procesos if proceso_1 else otros_procesos
    
    tareas = []
    tiempo_actual = 0  # Tiempo acumulado en la ejecución

    for i, proceso in enumerate(procesos_ordenados):
        pid, rafaga, tiempo_llegada, prioridad = proceso  # Extraer datos
        
        # Si es el primer proceso (Proceso 1), debe comenzar en 0
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
        mostrar_tabla_tiempos_espera(procesos_ordenados)
        mostrar_tabla_tiempos_sistema(procesos_ordenados)
    
    button.on_clicked(on_click)
    
    plt.show()
