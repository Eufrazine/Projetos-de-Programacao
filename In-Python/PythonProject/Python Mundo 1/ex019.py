# Sorteando um item na lista. Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quatro aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
# choice é escolher
print(f'O aluno escolhido foi {escolhido}')

# affe que daora isso kkkk
