# Exercício Python #007

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
# float pois são flutuantes also números com pontos. Ex: 4.5,-0.9, 7.0
print(f'A media entre {n1:.1f} e {n2} é igual a {(n1 + n2) / 2:.1f}')
# esse "":.1f"" significa que quero só 1 numéro após o número flutuante.
# Ex: 2.222 vai ficar 2.2, se fosse :.2f ficaria 2.22...
# >>>>eu sozinha fiz esse de cima, pensando em não usar mais que as variantes essenciais<<<<

# vi esse nos comentarios e amei kkkk

# print(' ====== Calcula média arintimética ======')
# print('Bem vindo de volta, estamos na sétima aula de exercícios')
# notaum = float(input('Nota um :'))
# notadois = float(input('Nota dois :'))
# media = (notaum + notadois) / 2
# if media >= 6.0:
#   print('A média entre : {:.1f} e : {:.1f} é : {:.1f}'.format(notaum, notadois, media))
# else:
#   print('Estudar que é bom ninguém quer né !!')
