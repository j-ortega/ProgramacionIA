import Leccion1
# Indexado/Slicing
print(Leccion1.indexado4letras("programación"))
print(Leccion1.indexadocada2letras("programación"))
print(Leccion1.invertida("programación"))
print(Leccion1.ultima3letras("programación"))

# Membership
palabras = ["ia", "python", "datos"]
print(Leccion1.pertenece(palabras[1], "py"))
print(Leccion1.pertenecelista(palabras, "ml"))
print(Leccion1.convertirSetPertenece(palabras, "datos"))
