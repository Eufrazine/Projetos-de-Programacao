# Seno, Cosseno e Tangente. Faça um programa que leia um ângulo qualuqer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
# eu uso o (randians(x)) pq o seno, cos, tan são calculados com o radiano do ângulo, acho.
print(f'O ângulo de {ang} tem o Seno de {seno:.2f}')
coss = cos(radians(ang))
print(f'O ângulo de {ang} tem o coss de {coss:.2f}')
tan = tan(radians(ang))
print(f'O ângulo de {ang} tem a tangente de {tan:.2f}')
