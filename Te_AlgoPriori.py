import matplotlib.pyplot as plt
import numpy as np
from AlgoPriori import tabla_AlgoPriori  # Importamos la función para obtener los datos

def mostrar_tabla_tiempos_espera(procesos):
    if not procesos:
        print("Error: No hay datos de procesos disponibles.")
        return
    
    # Ordenar procesos por prioridad (menor número = mayor prioridad)
    procesos.sort(key=lambda x: x[3])  

    tiempos_espera = []
    nombres_procesos = []
    tiempo_acumulado = 0
    
    for i, proceso in enumerate(procesos):
        pid, rafaga, tiempo_llegada, prioridad = proceso
        
        if i == 0:
            espera = 0  # El primer proceso no espera
        else:
            espera = max(0, tiempo_acumulado - tiempo_llegada)  # Espera en función del tiempo de llegada
        
        tiempo_acumulado += rafaga  # Sumar la ráfaga al tiempo acumulado
        nombres_procesos.append(f"P{pid}")  
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
