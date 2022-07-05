# Os operadores aritimeticos também servem para coisas alem de contas, segue o exemplo:
# print('= '*10)
# n = input('Qual é o seu nome? ')
# print(f'Prazer em te conhecer {n:=^20} !')
# print(f'Prazer em te conhecer, {n}!') # sem espaços
# print(f'Prazer em te conhecer, {n:20}!') # com 20 espaços
# ---------------------------------------------------------------------- #

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print(f'A soma vale {s}, o produto {m}, divisão {d:.3f}, divisão inteira {di} e a potência {e}')
# se eu tivesse duas linhas de prints mas não quero que quebre, é só eu colocar ,end='' no final
# quebrar a linha no meio é só colocar / n
