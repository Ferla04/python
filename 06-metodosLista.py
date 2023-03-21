# Crear una lista
lista = list('ABCD')

print(len(lista))

# -----------------------------
# APPEND: Agrega un elemento al array
lista.append('F') # --> muta el array
print(lista)

# INSERT: Agrega un elemento a partir de un indice
lista.insert(4, 'E')
print(lista)

# EXTEND: Une dos listas
lista2 = ['G', 'H', 'I']
# print([*lista, *lista2])
lista.extend(lista2)
print(lista)

# -----------------------------
# POP: Elimina un elemento a partir del indice
lista.pop(1)
lista.pop(-1) # -> Elimina el ultimo elemento
print(lista)

# REMOVE: Elimina un elemento apartir de su valor, si no encuentra el valor muestra un error
lista.remove('G')
print(lista)

# CLEAR: Elimina todos los elementos
# lista.clear()
# print(lista)

# -----------------------------
# SORT: Ordena los arrays que sus elementos sean los mismo tipos de datos
lista.append('B')
print(lista)
lista.sort()
print(lista)

listaNumeros = [1,2,7,4,6,3]
listaNumeros.sort()
print(listaNumeros)
listaNumeros.sort(reverse=True)
print(listaNumeros)

# REVERSE
lista.reverse()
print(lista)

# -----------------------------
# TUPLE: Crear una tupla apartir de un array
array = ['a', 'b', 'c']
print(tuple(array))