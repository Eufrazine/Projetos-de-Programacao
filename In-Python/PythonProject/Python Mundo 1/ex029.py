# ===ex029===
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velo = int(input('Qual é a velocidade atual do carro? '))
# print(velo)

""" Tentei assim kkk é não deu certo, okay eu quase acertei, era só fazer o *7, mas okay :D
if velo < 80:
    print('okay')
else:
    print('Puts, multado')
multa = velo-80 (pegar o resto e fazer vezes 7, 7 são os reias, pois a cada 10km são 70 reais
                 ex: 100-80 é igual a 20, 20*7 é 140, 20km a mais permitido e 140 reais de multa.
print(multa)"""

# Essa é uma condição simples
if velo > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velo-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
