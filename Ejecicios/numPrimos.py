def esPrimo(num):
  for i in range(2, num - 1):
    if num % i == 0:
      return False

  return True


def listaPrimos(limit):
  primos = []

  for i in range(2, limit + 1):
    esPrimo(i) and primos.append(i)

  return primos


# hdhd
resultado = listaPrimos(10)

print(resultado)
