# ===ex025===
# Crie um programa que leia o nome de uma
# pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

# tentei usando in, mas separado do primeiro "print" e não deu certo, assim:
# print('silva' in nome)
