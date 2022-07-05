# Exercício Python #004 - Dissecando uma Variável
# É o mesmo do desafio 4
# ------------------------------------------------ #

x = input('Digite algo: ')

# O MODO MAIS SIMPLES É ESSE=
print('O tipo primitivo desse valor é ', type(x))
print('Só tem espaços?', x.isspace())
print('É um número? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas? ', x.islower())
print('Está capitalizado? ', x.istitle())

# O MODO USANDO O .format OU SÓ f=

# print(f'O tipo primitivo desse valor é {type(x)}')
# print(f'Só tem espaços? {x.isspace()}')
# print(f'É um número? {x.isnumeric()}')
# print(f'É alfabético? {x.isalpha()}')
# print(f'É alfanumérico? {x.isalnum()}')
# print(f'Está em maiúsculas? {x.isupper()}')
# print(f'Está em minúsculas? {x.islower()}')
# print(f'Está capitalizado? {x.istitle()}')
