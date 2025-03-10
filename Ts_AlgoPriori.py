import matplotlib.pyplot as plt
import numpy as np
from AlgoPriori import tabla_AlgoPriori  # Importamos la función para obtener los datos

def mostrar_tabla_tiempos_sistema(procesos):
    if not procesos:
        print("Error: No hay datos de procesos disponibles.")
        return
    
    # Ordenar procesos por prioridad (menor número = mayor prioridad)
    procesos.sort(key=lambda x: x[3])  

    tiempos_sistema = []
    nombres_procesos = []
    tiempo_actual = 0  # Tiempo acumulado

    for proceso in procesos:
        pid, rafaga, tiempo_llegada, prioridad = proceso

        # Ajustar el inicio considerando si el proceso ya llegó o hay que esperar
        inicio = max(tiempo_actual, tiempo_llegada)
        fin = inicio + rafaga
        sistema = fin - tiempo_llegada  # Tiempo en el sistema
        
        tiempo_actual = fin  # Actualizar el tiempo acumulado

        nombres_procesos.append(f"P{pid}")
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
