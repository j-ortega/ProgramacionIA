
import ejercicio3


def main():

    # EJERCICIO 1: Crear array 5x5
    print("\nEJERCICIO 1: ARRAY 5X5")
    array = ejercicio3.crear_array_2d()
    print(array)

    # EJERCICIO 2: Normalizar array
    print("\nEJERCICIO 2: NORMALIZAR ARRAY")
    array_normalizado = ejercicio3.normalizar_array(array)
    print(array_normalizado)

    # EJERCICIO 3: Extraer valores mayores a 0.5
    print("\nEJERCICIO 3: VALORES MAYORES A 0.5")
    mayores = ejercicio3.extraer_mayores_05(array_normalizado)
    print(mayores)

    # EJERCICIO 4: Binarizar array
    print("\nEJERCICIO 4: BINARIZAR ARRAY")
    mascara, where = ejercicio3.binarizar_array(array_normalizado)

    print("Usando máscara booleana:")
    print(mascara)

    print("Usando np.where:")
    print(where)

    # EJERCICIO 5: Crear matriz 5x5
    print("\nEJERCICIO 5: MATRIZ DEL 0 AL 24")
    matriz = ejercicio3.crear_matriz_5x5()
    print(matriz)

    # EJERCICIO 6: Extraer diagonales
    print("\nEJERCICIO 6: DIAGONALES")
    diagonal_principal, diagonal_secundaria = ejercicio3.extraer_diagonales(matriz)

    print("Diagonal principal:")
    print(diagonal_principal)

    print("Diagonal secundaria:")
    print(diagonal_secundaria)

    # EJERCICIO 7: Crear matriz 6x4
    print("\nEJERCICIO 7: MATRIZ 6X4")
    matriz_6x4 = ejercicio3.crear_matriz_6x4()
    print(matriz_6x4)

    # EJERCICIO 8: Media de cada fila
    print("\nEJERCICIO 8: MEDIA DE CADA FILA")
    medias = ejercicio3.calcular_media_filas(matriz_6x4)
    print(medias)

    # EJERCICIO 9: Restar la media de cada fila
    print("\nEJERCICIO 9: BROADCASTING")
    resultado = ejercicio3.restar_media_filas(matriz_6x4)

    print("Forma de la matriz original:", matriz_6x4.shape)
    print("Forma del array de medias:", medias.shape)
    print("Forma de las medias adaptadas:", medias[:, None].shape)

    print("Matriz después de restar las medias:")
    print(resultado)

    # EJERCICIO 10: Crear DataFrame 3D
    print("\nEJERCICIO 10: DATAFRAME 3D")
    df = ejercicio3.crear_dataframe_3d()
    print(df)

    # EJERCICIO 11: Convertir DataFrame a NumPy
    print("\nEJERCICIO 11: CONVERTIR DATAFRAME A NUMPY")
    array_numpy = ejercicio3.dataframe_a_numpy(df)
    print(array_numpy)

    # EJERCICIO 12: Calcular distancia al origen
    print("\nEJERCICIO 12: DISTANCIA EUCLIDIANA AL ORIGEN")
    distancias = ejercicio3.calcular_distancia_origen(df)
    print(distancias)

    # EJERCICIO 13: Añadir distancia al DataFrame
    print("\nEJERCICIO 13: AÑADIR COLUMNA DISTANCIA")
    df = ejercicio3.añadir_distancia_al_dataframe(df)
    print(df)


if __name__ == "__main__":
    main()
