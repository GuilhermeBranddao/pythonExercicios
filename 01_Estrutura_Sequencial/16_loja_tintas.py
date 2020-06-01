tam = float(input("Digite aqui o tamanho da parede em metros quadrados da área a ser pintada: "))

tinta = tam / 3
print(tinta)
qtdL = tinta / 18
qtdRS = qtdL * 80
print("A quantidade de latas de tintas de 18L a serem compradas é {:.2f} ".format(qtdL))
print("O preço a ser pago é R${:.2f} ".format(qtdRS))
