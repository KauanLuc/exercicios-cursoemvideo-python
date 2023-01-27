from math import sin,cos,tan,radians
angulo = float(input('digite o angulo:'))
seno = sin(radians(angulo))
cosseno = cos (radians(angulo))
tangente = tan (radians(angulo))
print(' o angulo de {} tem o seno {:.2f}\n o angulo de {} tem cosseno de {:.2f}\n o angulo de {} tem tangente de {:.2f}'.format(angulo,seno,angulo,cosseno,angulo,tangente))