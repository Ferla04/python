# Falto el profe y los alumnos van a armar la clase
# Pedir el nombre y edad de los compañeros que vinieron a clase

def obtenerCompañeros():
  cantCompañeros = int(input('Cant de compañeros: '))
  compañeros = []

  for i in range(cantCompañeros):
    nombre = input(f'Nombre{i+1}: ')
    edad = int(input(f'edad de {nombre}: '))
    compañeros.append((nombre, edad))

  compañeros.sort(key=lambda compañero: compañero[1])

  asistente, _ = compañeros[0]
  profesor, _ = compañeros[-1]

  return f'El profesor es {profesor} y su asistente es {asistente}'

print(obtenerCompañeros())

# _, _, tres = (1, 2, 3)
# print(f' - {tres}')
