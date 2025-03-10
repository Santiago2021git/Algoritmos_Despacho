import matplotlib.pyplot as plt
import numpy as np
from Fifo import tabla_fifo 

def mostrar_tabla_tiempos_sistema(procesos):
    if not procesos:
        print("Error: No hay datos de procesos disponibles.")
        return
    
    # Listas para almacenar cálculos
    tiempos_sistema = []
    nombres_procesos = []
    rafagas = [p[1] for p in procesos]  # Lista con todas las ráfagas
    
    # Calcular los tiempos de sistema
    for i, proceso in enumerate(procesos):
        pid, rafaga, tiempo, prioridad = proceso
        sistema = sum(rafagas[:i+1]) - tiempo  # Suma de ráfagas hasta el proceso i, menos su tiempo de llegada
        nombres_procesos.append(f"P{pid}")  # Solo el identificador del proceso
        tiempos_sistema.append(sistema)
    
    # Calcular el tiempo de sistema promedio
    tiempo_promedio = sum(tiempos_sistema) / len(tiempos_sistema) if tiempos_sistema else 0
    
    # Datos para la tabla
    datos_tabla = list(zip(nombres_procesos, tiempos_sistema))
    datos_tabla.append(["Promedio", round(tiempo_promedio, 2)])
    
    # Crear la tabla
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.axis('tight')
    ax.axis('off')
    tabla = ax.table(cellText=datos_tabla, 
                      colLabels=["Procesos", "Tiempo de Sistema"], 
                      cellLoc='center', loc='center')
    
    plt.show()
