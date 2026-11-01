# Indexado/Slicing
def indexado4letras(palabra:str)->str:
       return palabra[:4]

def indexadocada2letras(palabra)->str:
       return palabra[1::2]

def invertida(palabra:str)->str:
       return palabra[::-1]

def ultima3letras(palabra:str)->str:
       return palabra[-3:]

# Membership
def pertenece(palabra:str, letra:str)->bool:
       return letra in palabra

def pertenecelista(palabra:list, letra:str)->bool:
       return letra in palabra

def convertirSetPertenece(palabra:list, letra:str)->bool:
       return letra in set(palabra)

# LEN

def longitud_lista(elementos: list) -> int:
    # Devuelve el número de elementos de la lista
    return len(elementos)

# CADENAS


def limpiar_cadena(texto: str) -> str:
    # Quita espacios del principio y del final
    return texto.strip()


def separar_cadena(texto: str) -> tuple:
    # Separa el texto utilizando la coma
    partes = texto.split(",")
    return tuple(partes)


def unir_cadenas(partes: tuple) -> str:
    # Une las partes con un guion
    return " - ".join(partes)

# CONDICIONALES


def clasificar_numero(numero: float) -> str:
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

# EJERCICIO 6: BUCLE FOR

def nombres_mas_4_letras(nombres: list) -> list:
    resultado = []

    for nombre in nombres:
        if len(nombre) > 4:
            resultado.append(nombre)

    return resultado

# BUCLE WHILE


def contar_hasta_stop() -> None:
    contador = 1

    while True:
        texto = input("Escribe stop para terminar: ")

        if texto == "stop":
            break

        print(contador)
        contador += 1

# EJERCICIO 8: NÚMEROS PARES

def obtener_pares(numeros: list) -> list:
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares

# EJERCICIO 9: FUNCIÓN ES_PAR

def es_par(numero: int) -> bool:
    return numero % 2 == 0

# *ARGS

def media(*numeros: float) -> float:
    if len(numeros) == 0:
        return 0.0

    return sum(numeros) / len(numeros)

# EJERCICIO 11: MAP Y LAMBDA

def celsius_a_fahrenheit(temperaturas: list) -> list:
    return list(map(lambda x: x * 9 / 5 + 32, temperaturas))

# EJERCICIO 12: FILTER

def nombres_empiezan_a(nombres: list) -> list:
    return list(filter(lambda nombre: nombre.startswith("A"), nombres))

# EJERCICIO 13: ZIP

def combinar_nombres_notas(nombres: list, notas: list) -> list:
    return list(zip(nombres, notas))

# EJERCICIO 14: ENUMERATE

def enumerar_ciudades(ciudades: list) -> list:
    return list(enumerate(ciudades, start=1))

# EJERCICIO 15: MAP Y FILTER

def transformar_filtrar_palabras(palabras: list) -> list:
    # Primero convierte las palabras a title case
    resultado = list(map(lambda palabra: palabra.title(), palabras))

    # Después selecciona las de 5 letras o más
    resultado = list(filter(lambda palabra: len(palabra) >= 5, resultado))

    return resultado

# EJERCICIO 16: VARIABLES TIPADAS

edad: int = 38

precios: list[float] = [10.5, 20.0, 30.75]

coordenadas: tuple[int, int] = (10, 20)

# EJERCICIO 17: MAYOR DE EDAD

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

# EJERCICIO 18: CONCATENAR

def concatena(a: str, b: str) -> str:
    if b is None:
        b = ""

    return a + b



# EJERCICIO 19: PROMEDIO


def promedio(valores: list) -> float:
    if len(valores) == 0:
        return 0.0

    return sum(valores) / len(valores)



# EJERCICIO 20: PROCESAR ENTERO O STRING


def procesar(valor) -> str:
    if isinstance(valor, int):
        return str(valor ** 2)
    else:
        return valor.upper()



# EJERCICIO 21: SUMA MIXTA


def suma_mixta(a, b) -> float:
    return float(a) + float(b)


def area_circulo(radio: float) -> float:
    return 3.1416 * radio ** 2



# EJERCICIO 24: FACTORIAL


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El número no puede ser negativo")

    resultado = 1

    for numero in range(1, n + 1):
        resultado = resultado * numero

    return resultado


def contar_lineas_archivo(path: str) -> int:
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            return len(lineas)

    except FileNotFoundError:
        print("El archivo no existe")
        return None



# EJERCICIO 27: LEER UN FLOAT DE UN FICHERO


def lee_float(path: str) -> float:
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

        return float(texto)

    except FileNotFoundError:
        return None

    # Si el contenido no es numérico, float()
    # lanza automáticamente ValueError.



# EJERCICIO 28: SET COMPREHENSION


def multiplos_de_3() -> set:
    return {numero for numero in range(21) if numero % 3 == 0}



# EJERCICIO 29: COMPREHENSION ANIDADA


def palabras_mayusculas(frases: list) -> list:
    return [
        palabra.upper()
        for frase in frases
        for palabra in frase.split()
    ]



# EJERCICIO 30: MINI-RETO ANALIZAR LOG


def analiza_log(path: str) -> dict:
    # Contadores de los tipos de registros
    niveles = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    tiempos = []
    usuarios = set()

    # Leemos el archivo línea por línea
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.split()

            if len(partes) != 3:
                continue

            # Ejemplo: INFO:
            nivel = partes[0].replace(":", "")

            # Ejemplo: usuario=ana
            usuario = partes[1].split("=")[1]

            # Ejemplo: tiempo=0.23
            tiempo = float(partes[2].split("=")[1])

            if nivel in niveles:
                niveles[nivel] += 1

            usuarios.add(usuario)
            tiempos.append(tiempo)

    # Calculamos el tiempo medio
    if len(tiempos) > 0:
        tiempo_medio = sum(tiempos) / len(tiempos)
    else:
        tiempo_medio = 0

    return {
        "niveles": niveles,
        "tiempo_medio": tiempo_medio,
        "usuarios": sorted(usuarios)
    }