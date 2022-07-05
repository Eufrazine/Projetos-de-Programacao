# ===ex035===
# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

# Não consegui fazer, mas já tinha colocado o "float(input)" direitinho 😎
print('∶∼∽∶' * 20)
print('Analisador de Triângulos')
print('∶∼∽∶' * 20)

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos {a:.0f}, {b:.0f} e {c:.0f}, PODEM formar um triângulo')
# Acima fiz do meu jeitnho pra ficar mais enfeitado.
# Esse é o jeito do Guanabara. print('Os segmentos acima PODEM formar um triângulo!')
else:
    print(f'Os segmentos {a:.0f}, {b:.0f} e {c:.0f}, NÃO PODEM formar um triângulo!')
# print('Os segmentos acima NÃO PODEM formar um triângulo!')

# Eu pensei que era BEM dificil mas não é tanto, é só saber fazer o calculo direitinho e entender.

""" Peguei dos coments: 
    
a = float(input('Coloque o valor de um lado: '))
b = float(input('Coloque o valor de outro lado: '))
c = float(input('Coloque o valor de outro lado: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
  print('Os lados {}, {} e {} podem formar triângulo.'.format(a, b, c))
else:
  print('Os lados {}, {} e {} não podem formar triângulo.'.format(a, b, c))"""
