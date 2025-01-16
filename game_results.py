import os
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from font_styling import *

ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resultados_juego.xlsx')

def guardar_resultados(nombre, modo, dificultad, resultado, puntaje):
    
    df = pd.DataFrame({
        'Nombre': [nombre],
        'Modo': [modo],
        'Dificultad': [dificultad],
        'Resultado': [resultado],
        'Puntaje': [puntaje]
    })

    # Convertir 'Dificultad' a texto
    df['Dificultad'] = df['Dificultad'].replace({1: 'Fácil', 2: 'Medio', 3: 'Difícil'})

    if os.path.exists(ruta_archivo):
        # Si el archivo existe, abrir el archivo y agregar los datos
        with pd.ExcelWriter(ruta_archivo, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            startrow = writer.sheets["Datos"].max_row
            # Escribir los datos sin encabezado
            df.to_excel(writer, sheet_name="Datos", startrow=startrow, index=False, header=False)
    else:
        # Si el archivo no existe, crear un nuevo archivo y escribir los datos
        with pd.ExcelWriter(ruta_archivo, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name="Datos", index=False)


def mostrar_estadistica(nombre):
    
    fecha_hora_actual = datetime.now()
    fecha_hora_f = fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n{verde}{negrilla}REVISIÓN DE LA JUGADA\n{reset}")
    print(f'Partida finalizada!\n{negrilla}Fecha y hora de finalización: {fecha_hora_f}{reset}')
    print("-------------------------------------------------")
    print(f'\n{negrilla}Jugador:{reset}{nombre}\n')

    if not os.path.exists(ruta_archivo):
        print(f'\n{rojo}El archivo no existe.{reset}\n')
        return

    # Leer el archivo Excel
    df = pd.read_excel(ruta_archivo, header=0)

    # Verificar que el DataFrame no esté vacío
    if df.empty:
        print(f'\n{rojo}No hay datos disponibles para mostrar estadísticas.{reset}\n')
        return
    else:
        # Filtrar filas con datos NaN
        df = df.dropna()

        # Lista para almacenar los elementos extraídos
        lista_modos = []
        lista_puntaje = []

        # Imprimir cada fila con el formato deseado
        for index in range(len(df)):
            fila_actual = df.iloc[index].values.tolist()  # Convertir la fila a lista

            # Extraer los valores de la fila
            modo_juego = fila_actual[1].lower() if isinstance(fila_actual[1], str) else str(fila_actual[1])
            dificultad = fila_actual[2].lower() if isinstance(fila_actual[2], str) else str(fila_actual[2])
            resultado = fila_actual[3]
            puntaje = int(fila_actual[4]) if isinstance(fila_actual[4], (np.int64, np.int32)) else fila_actual[4]

            # Almacenar los elementos extraídos en la lista
            lista_modos.append(modo_juego)
            lista_puntaje.append(puntaje)

            # Imprimir resultado de la partida
            print(
                f'En la partida {index + 1} en ({modo_juego}) con dificultad "{dificultad}": {rojo}{resultado}{reset}. Obtuviste {puntaje} pts.')

        puntaje_total = sum(lista_puntaje)
        if puntaje_total == 0:
            print(f'\nPuntuación total: {puntaje_total}\n')
            print(f'\nVuelvelo a intentar')
        else:
            df['Modo'] = lista_modos
            df['Puntaje'] = lista_puntaje
            resultados_agrupados = df.groupby('Modo')['Puntaje'].sum().reset_index()

            # Imprimir resultado de la partida
            print(f'{verde}{negrilla}Puntación total: {puntaje_total} pts.{reset}')


            # Graficar
            plt.figure(figsize=(12, 6))  # Ajustar el tamaño de la figura
            plt.bar(resultados_agrupados['Modo'].str.capitalize(), resultados_agrupados['Puntaje'], color='skyblue',
                    width=0.4)  # Ajustar el ancho de las barras
            plt.title(f'{nombre}\n Puntuación Total: {puntaje_total}', fontsize=13,
                      fontweight='bold')  # Mejorar el título
            plt.ylabel('Puntuación', fontsize=14, fontweight='bold')  # Etiqueta del eje Y
            plt.yticks(fontsize=12)  # Ajustar tamaño de fuente del eje Y
            plt.grid(axis='y', linestyle='--', alpha=0.7)  # Añadir una cuadrícula al eje Y
            plt.tight_layout()
            plt.show()