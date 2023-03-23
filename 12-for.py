# FOR EN ARRAYS, TUPLAS Y CONJUNTOS
animales = ['Perro', 'Gato', 'Loro', 'Pollo']
# IMPORTANTE: si cambio todos los arrays por tuplas o por connjuntos también funcionan

for animal in animales:
  print(animal)


# Iterar dos arrays al mismo tiempo
# Nota: Los dos arrays deben tener la misma longitud
nombres = ['Fer', 'Juan', 'Cami']
apellidos = ['Velasquez', 'Reyes', 'Solorza']

for nombre, apellido in zip(nombres, apellidos):
  print(f'Mi nombre es {nombre} {apellido}')

# Con Range
# for num in range(5, 10):
#   print(num)

# Forma NO optima - incorrecta y además no funciona en conjuntos
# for index in range(len(animales)):
#   print(animales[index])

# Forma correcta
for index in enumerate(animales):
  print(index[1])

# FOR-ELSE
for animal in animales:
  print(f'Es un animal: {animal}')
else:
  print('Terminó el bucle')


# Creacion de array que recibe sus itmes por iteracion
animalesPlurales = [x + 's' for x in animales]
print(animalesPlurales)

# FOR diccionario
diccionario = {
  'nombre': 'Fernanda',
  'apellido': 'Velasquez',
  'altura': '1.60'
}

for key in diccionario:
  print(diccionario[key])

# WHILE
# cont = 0
# while cont < 5:
#   print(cont)
#   cont += 1
