import leccion2 as leccion1

# EJERCICIO 1: INDEXADO / SLICING

print("EJERCICIO 1")
print(leccion1.indexado4letras("programación"))
print(leccion1.indexadocada2letras("programación"))
print(leccion1.invertida("programación"))
print(leccion1.ultima3letras("programación"))

# EJERCICIO 2: MEMBERSHIP
print("EJERCICIO 2")
palabras = ["ia", "python", "datos"]
print(leccion1.pertenece(palabras[1], "py"))
print(leccion1.pertenecelista(palabras, "ml"))
print(leccion1.convertirSetPertenece(palabras, "datos"))


# EJERCICIO 3: LEN
print("EJERCICIO 3")
elementos = [[], [1, 2], "ab"]
print(leccion1.longitud_lista(elementos))

# EJERCICIO 4: CADENAS
print("EJERCICIO 4")
texto = "  Python,3.12  "
limpio = leccion1.limpiar_cadena(texto)
print(limpio)
partes = leccion1.separar_cadena(limpio)
print(partes)
print(leccion1.unir_cadenas(partes))

# EJERCICIO 5: CONDICIONALES
print("EJERCICIO 5")
numero = float(input("Introduce un número: "))
print(leccion1.clasificar_numero(numero))


# EJERCICIO 6: BUCLE FOR
print("EJERCICIO 6")
nombres = ["Ana", "Carlos", "Luis", "Marta", "Elena"]
print(leccion1.nombres_mas_4_letras(nombres))

# EJERCICIO 7: BUCLE WHILE
print("EJERCICIO 7")
leccion1.contar_hasta_stop()

# EJERCICIO 8: NÚMEROS PARES
print("EJERCICIO 8")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(leccion1.obtener_pares(numeros))

# EJERCICIO 9: FUNCIÓN ES_PAR
print("EJERCICIO 9")
print(leccion1.es_par(8))
print(leccion1.es_par(7))

# EJERCICIO 10: *ARGS
print("EJERCICIO 10")
print(leccion1.media(10, 20, 30, 40))

# EJERCICIO 11: MAP Y LAMBDA
print("EJERCICIO 11")
temperaturas = [0, 10, 20, 30]
print(leccion1.celsius_a_fahrenheit(temperaturas))

# EJERCICIO 12: FILTER
print("EJERCICIO 12")
nombres = ["Ana", "Alberto", "Luis", "Andrea"]
print(leccion1.nombres_empiezan_a(nombres))

# EJERCICIO 13: ZIP
print("EJERCICIO 13")
alumnos = ["Ana", "Luis", "Marta"]
notas = [8.5, 7.0, 9.2]
resultado = leccion1.combinar_nombres_notas(alumnos, notas)
for alumno, nota in resultado:
    print("Alumno", alumno, "- Nota", nota)

# EJERCICIO 14: ENUMERATE
print("EJERCICIO 14")
ciudades = ["Madrid", "Granada", "Sevilla"]
resultado = leccion1.enumerar_ciudades(ciudades)
for posicion, ciudad in resultado:
    print(posicion, ciudad)

# EJERCICIO 15: MAP Y FILTER
print("EJERCICIO 15")
palabras = ["python", "ia", "datos", "programacion"]
print(leccion1.transformar_filtrar_palabras(palabras))

# EJERCICIO 16: VARIABLES TIPADAS
print("EJERCICIO 16")
print(leccion1.edad)
print(leccion1.precios)
print(leccion1.coordenadas)

# EJERCICIO 17: MAYOR DE EDAD

print("EJERCICIO 17")
print(leccion1.es_mayor_de_edad(20))
print(leccion1.es_mayor_de_edad(16))

# EJERCICIO 18: CONCATENAR
print("EJERCICIO 18")
print(leccion1.concatena("Hola", " mundo"))
print(leccion1.concatena("Hola", None))


# EJERCICIO 19: PROMEDIO
print("EJERCICIO 19")
valores = [10.0, 20.0, 30.0]
print(leccion1.promedio(valores))



# EJERCICIO 20: PROCESAR
print("EJERCICIO 20")
print(leccion1.procesar(5))
print(leccion1.procesar("python"))



# EJERCICIO 21: SUMA MIXTA
print("EJERCICIO 21")
print(leccion1.suma_mixta("10", 5))



# EJERCICIO 22: DOCSTRING
print("EJERCICIO 22")
help(leccion1.es_par)



# EJERCICIO 23: ÁREA DEL CÍRCULO
print("EJERCICIO 23")
print(leccion1.area_circulo(5))



# EJERCICIO 24: FACTORIAL
print("EJERCICIO 24")
print(leccion1.factorial(5))



# EJERCICIO 25: DOCSTRING DE MÓDULO
print("EJERCICIO 25")


# EJERCICIO 26: CONTAR LÍNEAS DE UN ARCHIVO
print("EJERCICIO 26")
print(leccion1.contar_lineas_archivo("datos.txt"))



# EJERCICIO 27: LEER UN FLOAT
print("EJERCICIO 27")
print(leccion1.lee_float("numero.txt"))



# EJERCICIO 28: SET COMPREHENSION
print("EJERCICIO 28")
print(leccion1.multiplos_de_3())



# EJERCICIO 29: COMPREHENSION ANIDADA

print("EJERCICIO 29")
frases = [
    "hola mundo",
    "python es genial",
    "list comprehensions"
]
print(leccion1.palabras_mayusculas(frases))



# EJERCICIO 30: ANALIZAR LOG
print("EJERCICIO 30")
print(leccion1.analiza_log("actividad.log"))
