# ===ex033===
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

# Verificando quem é o menor
"""if a<b and a<c:
    menor = a. 
Não tem problema fazer assim, mas já determinando o a como menor simplifica."""
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado foi {menor} e o maior {maior}!')
