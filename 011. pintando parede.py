largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
mq = largura * altura
qt = 0.5 * mq
print('Sua parede tem a dimensão de {:.1f}x{:.1f} e sua área é de {:.2f}m²'.format(largura, altura, mq))
print('Para pintar essa parede, você precisará de {:.1f}l de tinta.'.format(qt))





