# EXEMPLO 1 DA AULA====
# import math
# n = int(input('digite um número: '))
# raiz = math.sqrt(n)
# print(f'A rais de {n} é igual a {raiz:.2f}')
# ("identação" usando o math.(raiz)) print(f'A rais de {n} é igual a {math.floor(raiz)}')

# Usando o from import
from math import sqrt, floor
n = int(input('digite um número: '))
raiz = sqrt(n)
print(f'A rais de {n} é igual a {floor(raiz)}')
