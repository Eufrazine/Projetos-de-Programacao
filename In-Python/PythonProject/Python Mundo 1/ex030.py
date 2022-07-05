# ===ex030===
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

N = int(input('Me diga um número qualquer: '))
print(N)
if N % 2 == 0:
    print(f'O número {N} é PAR')
else:
    print(f'O número {N} é ímpar')

# % É o resto da divisão. EX: 5 dividido por 2, o resultado "//" é 2 e p resto "%" 1.

"""Como o Guanabara fez

número = int(input('Me diga um número qualquer: '))
#  reasultado = número % 2   #
print(f'O resultado foi {reasultado}')
if reasultado == 0:
    print(f'O número {número} é PAR')
else:
    print(f'O número {número} é ÍMPAR')"""
