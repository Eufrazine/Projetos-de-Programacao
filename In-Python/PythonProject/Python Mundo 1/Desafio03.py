n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1+n2

# print('A soma entre', n1, 'e', n2, 'é', s) esse é jeito "primordial" de fazer mostrar oq quero
# outro jeito logo abaixo:
# print('A soma entre {} e {} é {}'.format(n1, n2, s))
# outro jeito mais simples ainda:

print(f'A soma entre {n1} e {n2} é {s}')
