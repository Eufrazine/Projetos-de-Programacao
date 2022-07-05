# ===ex022===

nome = input(str('-Qual a sua graça? '))

# str para saber que é um conjunto de caracteres, mas acho que n precisa.

print('-Tudo em maiúsculo:', nome.upper())
print('-Tudo em minúsculo:', nome.lower())

print('-Quantas letras o seu nome tem, sem espaço:', len(nome) - nome.count(' '))

# Acredito que seja assim, len(nome) é quantas casas tem a frase toda e
# foi subtraida(-) pelo tanto de espaço (' '),

separa = nome.split()
print('-Seu primeiro nome tem {} letras'.format(len(separa[0])))
# Len seria a frase toda, foi dividida, pegou a primeira palavra (separa[0]) e contou com o len quantas letras tem.

# Guanabara também ensinou assim:
print('-Seu primeiro nome tem {} letras.'.format(nome.find(' ')))


# esse foi o jeito que entei fazer, o de cima peguei nos coments do yt kkkk :/
# print('-Quntas letras tem, sem espacço:',nome.strip())
# print('-quantas letras tem o primeiro nome:', nome.)

# vala que coisa dificil

# DEU CERTO AMEM
"""-Qual é o seu nome? Kim Taehyung Santos Da Silva Chaves
-Tudo em maiúsculo: KIM TAEHYUNG SANTOS DA SILVA CHAVES
-Tudo em minúsculo: kim taehyung santos da silva chaves
-Quantas letras tem, sem espaço: 30
-Quantas letras tem o primeiro nome: 3"""
