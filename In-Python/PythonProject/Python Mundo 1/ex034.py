# ===ex034===
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = int(input('Qual é o salário do funcionário? R$'))
Nsal = sal # Novo Salário

# 10% = x0,10. Ex no python: 10% igual a *0.10. N PODE , NO PYTHON EM
if sal >= 1250:
    sal = (sal*0.10) + sal
else:
    sal = (sal * 0.15) + sal

print(f'Quem ganhava R${Nsal:.2f} passa a ganhar R${sal:.2f} agora.')

# AFFE CONSEGUI FAZER SOZINHA 🥰🥰🥰🥰💜💜💜(corações roxos)😭😭😭🤩🤩🤩🥳🥳🥳🤧🤧🤧🎉🎉🎉🍾🍾🍾🥂🥂🥂🎂🎂🎂🌈🌈🌈🙏🙏🙏🙌🙌🙌
# Consegui fazer sem ajuda, quer dizer, olhei como o resultado ficou do prof e fui fazendo fiz.
# Usei o jeito, vamos por partes, primeiro fiz se o resultado das duas contas deram e certo e fui fazendo 😉

# Guanabara usou o jeito de  / em vez de *, abaixo como ele fez:

"""salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário*15/100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f} agora.')"""
