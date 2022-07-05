# Esse joguinho foi feito com a intenção de aprender e se divertir com o python, sem a intenção de ofender qualquer amante do palmeiras, e todos sabem que o palmeiras é um ótimo time 👍

# Peguei dos cometarios da aula 11 kkkk

# Para quem gosta de futebol para dar uma destraida ae :D

from emoji import emojize
#                                ↱ tudo sublinhado e em branco
time = str(input('\033[4;97mDigite o nome do seu time:\033[m ')).capitalize().strip()

if time == 'Palmeiras':
    print(emojize(f'Vishe, o \033[1;32mPALMEIRAS\033[m não tem nenhum mundial :beaming_face_with_smiling_eyes: \033[m'))
#                              ↳ Palmerias em verde e negrito                       ↳ emoji 😁
else:
    mund = int(input('\033[4;36mEscreva quantas vezes seu time tem um mundial:\033[m '))
#                                  ↳ tudo sublinhado e em ciano
    print(emojize(f'Parabéns o \033[1m{time}\033[m tem \033[1m{mund}\033[m mundiais :glowing_star:'))
#                                    ↳ time e mund em negrito                          ↳ emoji 🌟


# Dei uma mera modificada hihi
