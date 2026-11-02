import numpy as np
import pandas as pd

## Ejercicio 1 Crea un array 2D de forma `(5, 5)` con números aleatorios entre 0 y 50.
def crear_array_2d():
    return np.random.randint(0, 51, size=(5, 5))

## Ejercicio 2 Normalízalo al rango [0, 1] restando el mínimo y dividiendo entre el máximo ((valor - min) / (max - min)).
def normalizar_array(array):
    min_val = np.min(array)
    max_val = np.max(array)
    return (array - min_val) / (max_val - min_val)

## Ejercicio 3 Usa una **máscara booleana** para extraer únicamente los elementos mayores a 0.5.
def extraer_mayores_05(array):
    return array[array > 0.5]

## Ejercicio 4 (Extra) **Binariza** el array normalizado:  
   ## - Los valores > 0.5 deben pasar a 1.  
   ## - Los valores ≤ 0.5 deben pasar a 0.  
   ## - Hazlo de dos formas:  
   ## - Usando una máscara booleana.  
   ## - Usando `np.where`. 
def binarizar_array(array):
    # Usando máscara booleana
    binarizado_mascara = np.zeros_like(array)
    binarizado_mascara[array > 0.5] = 1
    
    # Usando np.where
    binarizado_where = np.where(array > 0.5, 1, 0)
    
    return binarizado_mascara, binarizado_where

## Ejercicio 5 Crea una matriz de 5x5 con los valores del 0 al 24.  
def crear_matriz_5x5():
    return np.arange(25).reshape(5, 5)

## Ejercicio 6 Extrae:  
   ##- La **diagonal principal**.
   ##- La **diagonal secundaria**.
   ## Muestra cada resultado por separado.
def extraer_diagonales(matriz):
    diagonal_principal = np.diagonal(matriz)
    diagonal_secundaria = np.diagonal(np.fliplr(matriz))
    return diagonal_principal, diagonal_secundaria

## Ejercicios (Broadcasting con filas)
## Ejercicio 7 Crea una matriz 6x4 de enteros aleatorios entre 0 y 20.
def crear_matriz_6x4():
    return np.random.randint(0, 21, size=(6, 4))

## Ejercicio 8  Calcula la media de cada fila.
def calcular_media_filas(matriz):
    return np.mean(matriz, axis=1)

## Ejercicio 9 Resta a cada elemento de la matriz la media de su fila usando **broadcasting** (sin bucles).
## Explica:
   ## - La forma de cada array antes de la operación.  
   ## - Cómo NumPy aplica las reglas de broadcasting.
def restar_media_filas(matriz):
    media_filas = calcular_media_filas(matriz)
    # La forma de la matriz original es (6, 4)
    # La forma del array de medias es (6,)
    # NumPy aplica broadcasting expandiendo la forma del array de medias a (6, 1) para que coincida con la forma de la matriz original.
    return matriz - media_filas[:, np.newaxis]

## Ejercicio 10 Crea un DataFrame con columnas `"x"`, `"y"`, `"z"` conteniendo 6 puntos en 3D generados aleatoriamente.
def crear_dataframe_3d():
    data = np.random.rand(6, 3)  # 6 puntos en 3D
    df = pd.DataFrame(data, columns=["x", "y", "z"])
    return df

## Ejercicio 11 Convierte ese DataFrame a NumPy con `.to_numpy()`.
def dataframe_a_numpy(df):
    return df.to_numpy()

## Ejercicio 12 Calcula la **distancia euclidiana** de cada punto al origen (0,0,0) usando NumPy.  
def calcular_distancia_origen(df):
    puntos = df.to_numpy()
    distancias = np.linalg.norm(puntos, axis=1)
    return distancias

## Ejercicio 13 Añade la distancia como nueva columna `"distancia"` al DataFrame original.
def añadir_distancia_al_dataframe(df):
    distancias = calcular_distancia_origen(df)
    df["distancia"] = distancias
    return df