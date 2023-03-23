import sys
import os

# Importar una funcion de un nivel mas alto (carpetas)
# ALTERNATIVAS python-path
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from modulo import saludar
saludar()

# Uso de esta funcion en un nivel más alto
def animar(name='Bruce'):
  print(f'tu puede {name}')
