# ===ex031===
# esenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# EU fiz assim e deu certo 🥰 e eu até acertei na hora de colocar o float :D

km = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {km}Km')
if km > 200:
    preço = km * 0.45
    print(f'E o preço da sua passagem será de R${preço:.2f}')
else:
    preço = km * 0.50
    print(f'E o preço da sua passagem será de R${preço:.2f}')

# Como o Guanabara fez
"""distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <=200: # menos ou igual
    preço = distância * 0.50
else:
    preço = distância * 0.45
--------------------------------------------------------------------
Do jeito "if simplificado" :
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'. format(preço))"""

# Nesse a conta vai direto no print, muito legal essa alternativa.
""" 
Peguei dos comentarios: 
Assim tbm funciona! ;)
--------------------------------------------------------------------
km = float(input('Qual a distância em (Km) você deseja percorrer? '))
if km <= 200:
    print('Sua passagem vai custar {} reais. '.format(km * 0.5))
else:
    print('Sua passagem vai custar {} reais. '.format(km * 0.45))
--------------------------------------------------------------------
# Usando o f (ainda mais simples):
if km <= 200:
    print(f'Sua passagem vai custar {km * 0.5} reais.')
else:
    print(f'Sua passagem vai custar {km * 0.45} reais.')"""
