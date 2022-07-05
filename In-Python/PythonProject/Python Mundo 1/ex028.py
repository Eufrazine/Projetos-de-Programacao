# ===ex028===
#  Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#  descobrir qual foi o n escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# não tenho a minima ideia de como fazer isso kkkk tive que ver o vídeo mesmo :/

# OKAY EU ATÉ CONSEGUI KKAAAAA só não sabia oq colocar no começo, mas o prof colocou o import,
# dai por diante consegui sozinha, o bruto claro, as decoraçoes e frases fui adicionando confomr fui vendo a aula.

from random import randint
from time import sleep
# é um metodo pra fazer o pc "dormir" ou esperar mesmo

computador = randint(0, 5)      # Faz o computador "Pensar"
# print(computador)             coloquei isso só para ver se estava dando certo.
print('\033[97m∶∼∽∶∶∼∽∶∶∼∽∶JOGO DE ADIVINHAÇÃO 1.0∶∼∽∶∶∼∽∶∶∼∽∶\033[m')
print('∶∼∽∶' * 20)               # Essa decoração repetida 20 vezes.
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('∶∼∽∶' * 20)

eu = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if eu == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {eu}!')


""" Peguei dos coments:
O meu deu certo, mais eu usei o choice...

from random import choice
print('-=-'* 19)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-'* 19)
lista=[0,1,2,3,4,5]
escolha=choice(lista)
n1=int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if n1 == escolha:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(escolha,n1))
print('--FIM--')"""
