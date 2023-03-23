def crearContraseña(num):
  chars = "abcdefghij"
  numeroString = str(num)
  num = int(numeroString[0])

  c1 = num - 2
  c2 = num
  c3 = num - 5

  return f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"

# print(crearContraseña(98))

# Parametros args
def suma(*numeros):
  return sum(numeros)


print(suma(2, 3, 4, 5))

# FUNCION LAMBDA
multiplicar = lambda x: x * 2
print(multiplicar(5))

esPar = lambda x: 'par' if x % 2 == 0 else 'impar'
print(esPar(5))

numeros = [1, 2, 3, 4, 5, 6]
numerosPares = filter(lambda x: x % 2 == 0, numeros)
print(list(numerosPares))
