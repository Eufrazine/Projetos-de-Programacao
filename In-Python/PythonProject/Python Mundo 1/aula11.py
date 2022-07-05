# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus
# programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

#  ↱ contra barra, do lado do shift. >>m MINÚSCULO<<
# \033[>CÓDIGO DA COR<m

# style= se está em negrito etc
# text= cor da fonte
# back, cor do fundo
# Na vdd pode colocar em qualquer ordem, pois tem diferença de codigo entre cd um.

"""
style         text        back
0 none        30 preto   | As mesma cores do text,
1 bold        31 vermelho | mas em vez de 30 é 40.
4 underline   32 verde    |
7 negative    33 amarelo |
              34 azul    |
              35 magenta |
              36 ciano  |
              37 cinza  |
              97  branco| 107 branco
"""

# print('\033[31;43mOlá, Mundo!\033m') ISSO EM VERMELHO E FUNDO AMARELO, esse ultimo é para o fundo não ir até o final.

print('\033[1;30;97mOlá, Mundo!\033[m')
# que estranho, to 30 ta como preto ué. Vi nos comentarios do vídeo e a lista de cores foi atualizada.

print('\033[30m∶∼∽∶\033[m' * 20)

a = 3
b = 5
print(f'Os valores são \033[31m{a}\033[m e \033[35m{b}\033[m!!!')

print('\033[97m∶∼∽∶\033[m' * 20)

nome = 'Monique'
print('Olá! Muito prazer em te conhecer, {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))

print('\033[37m∶∼∽∶\033[m' * 20)

# Esse é um jeito de se fazer usando o .format Assim fica mais separado. Vou tentar fazer usando só o f:
print(f'Olá! Muito prazer em te conhecer, \033[1;32m{nome}\033[m !!!')
# Deu certo só desse jeito 🤷‍😉

print('\033[35m∶∼∽∶\033[m' * 20)

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'pretoEbranco': '\033[7;97m'}
print('Olá! Muito prazer em te conhecer, {}{}{} !!!'.format(cores['pretoEbranco'], nome, '\033[m'))

print('\033[36m∶∼∽∶' * 20)
