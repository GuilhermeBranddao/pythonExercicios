area = float(input("Digite o temanho da area em metros quadrados: "))
cobertura = area / 3

qtdL18 = cobertura / 18
qtdR = cobertura % 18
print(qtdR)

qtdL3_5 = cobertura / 3.5

if(qtdL18 > 18):
    totRS18 = qtdL18 * 80
    print("Comprar apenas latas de 18")
elif(qtdL3_5 > 3.5 and qtdL3_5 < 18):
    totRS3_5 = qtdL3_5 * 25
    print("Comprar apenas latas de3.5")
else:
    print("Pouca tinta irmão")
