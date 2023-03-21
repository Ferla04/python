saludo = 'Hola Mundo'

# DIR: Devuelve una lista de atributos y metodos válidos
funcion = dir(saludo) #Funcion

# -----------------------------
mayus = saludo.upper()
minus = saludo.lower()
capitalL = saludo.capitalize() # <- primera letra en mayus
print(f'{mayus} - {minus} - {capitalL}')

# -----------------------------
# FIND o INDEX: Busca la primera coincidencia y retorna el indice donde se encuentra
print(saludo.find('z'))
print(saludo.index('a'))

# DIFERENCIA: Si no se encuentra una coincidencia el FIND retorna -1 y el INDEX genera un error

# -----------------------------
numero = '4'.isnumeric()
alpha = 'fer'.isalpha() #Caracteres de la a hasta z
alphaN = '4f'.isalnum()
print(f'{numero} - {alpha} - {alphaN}')
# NOTA: El espacio, *, /, - etc.. son caracteres especiales

# -----------------------------
# COUNT: cuenta el total de coincidencias
print(saludo.count('o'))
print(saludo.count('z'))

# LEN: cantidad de caracteres del string
print(len(saludo))

# -----------------------------
print(saludo.startswith('Hola'))
print(saludo.endswith('Hola'))

# -----------------------------
print(saludo.replace('Hola', 'Buenas'))

# -----------------------------
#SPLIT: Vuelve un string a un array, recibe como argumento el caracter pro el 
# que va a hacer las separaciones, NO acepta caracteres vacios '', y para 
# separar por caracter usar la funcion list
split = saludo.split()

#LIST
lista = list(saludo)

print(f'{split} vs {lista}')