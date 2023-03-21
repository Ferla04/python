diccionario = {
  'nombre': 'Fernanda',
  'apellido': 'Velasquez',
  'año': 2023
}

llaves = diccionario.keys()
print(llaves)

# -----------------------------
# GET: Si no escuentra la llave retorna none
valor = diccionario.get('apellido')
print(valor)

# []: Si no escuentra la llave genera Error 
# diccionario['apellido2']

# -----------------------------
# CLEAR: ELIMINA TODOS LOS ELEMTOS
# diccionario.clear()

# -----------------------------
# POP: Elimina el un elemento apartir de la llave
diccionario.pop('año')
print(diccionario)

# -----------------------------
# ITEMS: vuelve un diccionario iterable
diccionario2 = diccionario.items()
print(diccionario2)