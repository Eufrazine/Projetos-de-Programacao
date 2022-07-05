# ===ex027===
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
# print(nome)
print(f'Muito prazer em te conhecer {n}!')

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

# O "len" mostra quantas possiçoes tem a variavel, no caso "nome, -1 pois ele conta o 0, assim fica certinho.
# Não precisa escrever len(nome)-1. basta escrever nome[-1], mas assim fica mais facil de entender.

"""dividio = nome.split()
print(f'Seu primeiro nome é {dividio[0]}')
print(f'Seu último nome é {dividio.rfind[0]}') 
Eu tentei desse jeito, quase acertei em kkkkk"""


