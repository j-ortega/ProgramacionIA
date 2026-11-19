
from pathlib import Path
import joblib

CARPETA = Path(__file__).resolve().parent

modelo = joblib.load(CARPETA / "modelo_patentes.joblib")
vectorizador = joblib.load(CARPETA / "vectorizador_tfidf.joblib")

print("=== CLASIFICADOR DE PATENTES ===")
print("Escribe 'salir' para terminar.\n")

while True:

    titulo = input("Introduce el título de la patente: ").strip()

    if titulo.lower() == "salir":
        print("Programa finalizado.")
        break

    if not titulo:
        print("Debes introducir un título.\n")
        continue


    titulo_tfidf = vectorizador.transform([titulo])


    prediccion = modelo.predict(titulo_tfidf)

    print(f"\nCategoría predicha: {prediccion[0]}\n")
