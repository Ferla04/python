def fibonacci(limit):
  init = [0, 1]

  while True:
    sum = init[-1] + init[-2]
    if sum > limit:
      break

    init.append(sum)

  return init

print(fibonacci(6))
