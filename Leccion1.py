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