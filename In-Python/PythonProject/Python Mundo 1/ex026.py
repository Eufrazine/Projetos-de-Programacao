# ===ex026===
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
# é muito importante o uso do .strip, pois assim evita que os espaços deem erro.
print(frase)

"""print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letras A aparece na posição {}'.format(frase.find('A')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))"""

# Sem o .format
print(f'A letra "A" aparece {frase.count("A")} vezes na frase')
print(f'A primeira letras "A" aparece na posição {frase.find("A")+1}')
# Esse +1 foi só para ficar mais legivel para nós.
print(f'A última letra "A" apareceu na posição {frase.rfind("A")+1}')
# rfind pois assim ele começa a procurar do lado direito, right= direito
# find, mostra em que posição está o caractere escolhido, no caso 'A' mas poderia ser uma palavra.
