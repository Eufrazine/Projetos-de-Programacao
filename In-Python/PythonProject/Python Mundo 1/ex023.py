# ===ex023===
# Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.

n = int(input('Informe um número: '))
print(f'Analisando o número {n}')

""""O programa aparece a mensagem erro caso o usuário ultrapasse os
    4 algarismos. (peguei nos coments do yt)
    
 formatado = n.replace(' ', '')
 if len(formatado) > 4:
    # print('Erro. Só são permitidos números de 4 algarismos')
 else:
    if len(formatado) == 4:"""

# Jeito do Guanabara, desse jeito,
# evita o erro se não colocar um número de 4 casas.
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

"""print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')"""

""" Primeiro jeito que fiz, acima é só ele "resumido"
print('Unidade: {} '.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0])) """
