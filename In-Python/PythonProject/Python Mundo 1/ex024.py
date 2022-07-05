# ===ex024===
# Crie um programa que leia o nome de
# uma cidade diga se ela começa ou não com o nome "SANTO".


cid = str(input('Digite o nome de uma cidade: ')).upper().strip()
print(cid)

# print(cid.find('Santo')) TENTEI ASSIM MAS NÃO CERTO, pensei em usar "in" tbm

# O jeito do Guanabara, só coloquei o "capitalize" par ficar mais bonito
print(cid[:5] == 'Santo')

# Usando o "in", mas não é tão bom assim
# print('SANTO' in cid)

""" Comentariodo yt:
cidade = input('Em que cidade você nasceu? ').title().split()
print(cidade[0] == 'Santo')
Não tive problema com espaços excedentes dessa forma porque o split é feito excluindo os espaços e 
criando a lista apenas com as cadeias de caracteres. Achei mais simples que o dele"""