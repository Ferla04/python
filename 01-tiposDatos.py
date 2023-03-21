# DATOS SIMPLES
# Texto - string
'string'
'''colocar string
muti linea'''

# numero 
4 #int
4.4 #float
print('a' * 2)
print(4 * 2)


# booleanos
True
False

# DATOS COMPUESTOS
# array, tuplas, conjunto (set)
lista = ['Juan', 'Camila', 'Fernanda']
print(lista)

# tres maneras de crearlo
tupla = ('Juan', 'Camila', 'Fernanda')
tupla2 = tuple(lista)
tupla3 = 'Juancho','Cam','Fer'
print(tupla[0])

# Crearlo
conjunto = {'Juan', 'Camila', 'Fernanda', 'Fernanda'}
conjunto2 = set(lista)
# !Error: conjunto[1]
print(conjunto)

# DIRERENCIAS: 
# 1. Las tuplas y los conjuntos son inmodificables 
# 2. En los conjuntos no se pueden acceder a los elementos por el indice 
# 3. Los conjuntos eliminan elementos duplicados 
# 4. Usar las tuplas cuando son datos de lectura

# diccionario (dict)
diccionario = {
  'nombre': 'Fernanda',
  'apellido': 'Velasquez',
  'altura': '1.60'
}
print(diccionario['altura'])
