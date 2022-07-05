#  Tocando um MP3.
#  Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
"""import pygame
pygame.init()
pygame.mixer.music.load('SweetNight.mp3')
pygame.mixer.music.play()
pygame.event.wait()"""

# Para quem está com tudo igual ao exemplo do professor Guanabara, mas não sai som (sem nenhum código de erro):
# Por alguma incompatibilidade com o seu sistema, quando o pygame é inicializado,
# ele requer mais coisas do que estamos dando. A alternativa mais fácil é utilizarmos apenas o mixer e
# procurarmos outra forma de manter o programa funcionando, como import time junto com time.sleep(x) ou apenas um input.
# Aqui vai minha sugestão para não precisarmos importar mais nada e conseguirmos testar o som:
from pygame import mixer
mixer.init()
mixer.music.load('sweetnight.mp3')
# exclui esse audio, é só baixar outro e linkar aqui.
mixer.music.play()
opção = input('Quer parar de tocar essa música? [ 1 ] SIM \nEscolha uma opção: ')
if opção == 1:
    mixer.music.stop()
"""else:
    print('\033[35mAgora é so curtir a vibe ✌')
    mixer.music.play() # queria muito que isso funcionasse, mas não ta pegando :( 
    amanha tento ver nos comets da aula se alguem conseguiu fazer"""

# Já vimos todas estas linhas no curso, logo acredito ser a melhor solução até o momento.

"""opção = input('Quer tocar essa música? [ 1 ] SIM [ 2 ] NÃO\nEscolha uma opção: ')
if opção == 1:
mixer.init()
mixer.music.load('sweetnight.mp3')
mixer.music.play()
elif opção == 2:
mixer.music.stop()"""

# Ta aparecendo o codigo(?) da musica não sei pq, antes tava um ? antes ué

# pensei em usar o While, mas não sei como.
