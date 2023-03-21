# Creando duccuinarios 
diccionario = dict(nombre='Fer', apellido='velasquez')
print(diccionario)

# Las tuplas pueden ser llaves de los diccionarios
diccionario = {('Hola', 'Mundo'): 'Fernanda'}
print(diccionario)

# Los conjuntos o arrays tambien pueden ser llaves
# Solo tienen ser inmutables y eso se hace con el frozenset
# diccionario = {frozenset(['Hola', 'Mundo']): 'Fer'}

# creando diccionarios con fromKeys()
diccionario = dict.fromkeys(['nombre', 'apellido']) # --> default None
diccionario = dict.fromkeys(['nombre', 'apellido'], 'Nose')

print(diccionario)