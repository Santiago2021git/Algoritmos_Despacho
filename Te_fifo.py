import matplotlib.pyplot as plt
import numpy as np
from Fifo import tabla_fifo  # Importamos la función para obtener los datos


def mostrar_tabla_tiempos_espera(procesos):
    if not procesos:
        print("Error: No hay datos de procesos disponibles.")
        return
    
    # Listas para almacenar cálculos
    tiempos_espera = []
    nombres_procesos = []
    tiempo_acumulado = 0
    
    # Calcular los tiempos de espera
    for i, proceso in enumerate(procesos):
        pid, rafaga, tiempo, prioridad = proceso
        if i == 0:
            espera = 0 - tiempo  # El primer proceso siempre inicia con tiempo de espera 0
        else:
            espera = tiempo_acumulado - tiempo  # Se resta el tiempo ingresado por el usuario
        
        tiempo_acumulado += rafaga  # Acumular la ráfaga
        nombres_procesos.append(f"P{pid}")  # Solo el identificador del proceso
        tiempos_espera.append(espera)
    
    # Calcular el tiempo de espera promedio
    tiempo_promedio = sum(tiempos_espera) / len(tiempos_espera) if tiempos_espera else 0
    
    # Datos para la tabla
    datos_tabla = list(zip(nombres_procesos, tiempos_espera))
    datos_tabla.append(["Promedio", round(tiempo_promedio, 2)])
    
    # Crear la tabla
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.axis('tight')
    ax.axis('off')
    tabla = ax.table(cellText=datos_tabla, 
                      colLabels=["Procesos", "Tiempo de Espera"], 
                      cellLoc='center', loc='center')
    
    plt.show()
