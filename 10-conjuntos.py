# !Genera un error, ya que si hay en el elemento iterable(parametro)
# un array, ese array se pueden mutar y por lo tanto no se puede hasear 
# set(['dato1', 'dato2', ['array1', 'array2']])

# CORRECTO: solo se pueden meter tuplas
conjunto = set(['dato1', 'dato2', ('array1', 'array2')])
print(conjunto)


# Pero si queremos que ingresar tipos de datos como arrays, conjuntos,
# diccionarios al set, podemos hacer esto

mujeres = frozenset({'Fer', 'Cami', 'Dani'}) # --> crea un conjunto inmutable
sociedad ={'Juan', 'Cris', mujeres}
print(sociedad)


# TEORIAS DE CONJUNTOS
conjunto1 = {1,3,5,7} # -->superconjunto de conjunto2
conjunto2 = {1,3,7} # -->subconjunto de conjunto1


resultado = conjunto2.issubset(conjunto1)
# OTRA SINTAXIS: resultado = conjunto2 <= conjunto1
print(f'conjunto2 es un subconjunto de conjunto1? {resultado}')

resultado = conjunto1.issuperset(conjunto2)
# OTRA SINTAXIS: resultado = conjunto2 > conjunto1
print(f'conjunto1 es un superconjunto de conjunto2? {resultado}')

# Verificar si hay algún nuúmero en común, 
# retorna True cuando ningun elemento coincide
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)