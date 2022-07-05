d = float(input('Digite uma distancia em metros: '))
# mm = d * 1000 (Milímetros)
# cm = d * 100  (Centímetros)
# dm = d * 10   (Decímetros)
# dam = d / 10  (Decâmetros)
# hm = d / 100  (Hectómetros)
# km = d / 1000 (Quilômetros)
# print(f'A medida de {d}m corresponde a {cm:.0f}cm e {mm:.0f}mm.')

# formas de medidas em ordem são; km, hm, dam, m, dm, cm e mm

# ABAIXO sem usar variaveis=
print(f'A medida de {d}m corresponde a \n{d*1000:.0f}mm \n{d*100:.0f}cm \n{d*10:.0f}dm \n{d/10:.1f}dam \n{d/100:.2f}hm \n{d/1000:.3f}km.')
