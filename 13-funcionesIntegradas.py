numeros = [1, 2, 3, 4, 5, 6]

# MAX - MIN
print(f'max - {max(numeros)} | min - {min(numeros)}')

# SUM
print(sum(numeros))

# ROUND
# Redondeando un número a 2 decimales
numero = round(12.3456 * 100) / 100
print(numero)

# Pero round tiene otro parametro que sirve para darnos
# la cantidad de decimales al retornar
print(round(numero, 2))

# BOOL: Retorna False si los parametros son los siguientes:
# False, 0, Vacio, None (ninguno)
print(bool([]))

# ALL: Retorna True si todos los valores son verdaderos
print(all(['fer', 18, []]))
