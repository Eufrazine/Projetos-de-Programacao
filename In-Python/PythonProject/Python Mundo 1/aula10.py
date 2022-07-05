"""nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Qur nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
Acima é uma condição composta, se tiver só o 'if' ai é simples"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}.')
# sem o 'f' do m:.1f deu "A sua média foi 6e+00" ué kkkk
""" Condição composta:
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')"""
# Simples:
print('PARABÉNS!'if m >=6 else'ESTUDE MAIS!')


