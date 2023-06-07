from Esfera import Esfera


bola1 = Esfera('vermelha',4)
bola2 = Esfera('azul',7)
print(f'O volume da bola 1 é{bola1.volume()}cm^3')
print(f'A área superﬁcial da bola 1 é{bola1.area()}cm^2')
print(bola1.volume())
print(Esfera.volume(bola1))
