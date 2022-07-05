nome = input('Qual é o seu nome?')

# input é leia, ent ele vai ler a pergunta e vc responder, a reposta é o valor da variavel nesse caso *nome*

print('Prazer em te conhecer ', nome, '!')

# OUTRO EXEMPLO
print('É um prazer te conhecer, {}!'.format(nome))

# .format() substitui {}, como no exemplo acima :D') #Outro jeito ainda mais simples é o uso de "f".
# ex: print(f'É um prazer te conhecer, {nome}!'). Como visto, é só colocar a variavel dentro do {}.
print(f'É um prazer te conhecer, {nome}!')
