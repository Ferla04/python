archivoSinLeer = open('archivos/textos.txt')
# Error con los caracteres = open('archivos/textos.txt', encoding='UTF-8')
# archivo = archivoSinLeer.read() -> solo se puede leer una vez

lineas = archivoSinLeer.readlines()
print(lineas)
