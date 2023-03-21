from datetime import datetime

nombre = input('Dame tu nombre:')
edad = input('Dame tu edad:')
print(f'Hola {edad}, tienes {nombre} años')

nacimiento = int(input('Dame año de nacimiento:'))
añoActual = datetime.now().year
print(añoActual - nacimiento)