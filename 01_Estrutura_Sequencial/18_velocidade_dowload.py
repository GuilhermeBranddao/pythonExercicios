MB = float(input("Digite o tamanho do arquivo em MB: "))
Mbps = float(input("Digite o tamanho do arquivo em Mbps: "))
vel = (MB / Mbps) / 60
print("O temp aproximado do download é {:.1f} Minutos".format(vel))
