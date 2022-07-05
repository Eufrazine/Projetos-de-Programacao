# Catetos e Hipotenusa. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente,
# de um retangulo, calcule e mostre o comprimento da hipotenusa.

# formula, maneira matematica de se revolver:
"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2+ca**2)**0.5
outro jeito de se fazer=(1/2), acho.
print(f'A hipotenusa vai medir {hi:.2f}')"""

# usando o import:
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca) # (x,y) coisa lá de hipotenusa
print(f'A hipotenusa vai medir {hi:.2f}')
