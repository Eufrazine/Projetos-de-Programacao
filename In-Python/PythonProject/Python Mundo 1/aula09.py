# ===aula 09===

frase = 'Curso em Vídeo Python'
dividido = frase. split()
print(dividido[2][3])
# aqui é assim; me pegue a pegue o 2 (Vídeo) me mostre a letra 3, que no caso é o e

# dividido = frase.split()
# print(dividido[0])
# Desse jeito acima,
# podemos criar uma lista com a frase e selecionar a primeira palavra,
# no caso Curso, que começa na posição 0.

# ====================================================
# Para textos muito grandes, podemos usar as 3 aspas,""", e colocar um print antes,
# assim ele juntara o texto inteiro, em vez de dar print em todas as linhas. Ex:

# print("""Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(),
# transformações com replace(), upper(), lower(),
# capitalize(), title(), strip(), junção com join().""")
